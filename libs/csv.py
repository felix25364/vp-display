import asyncio
import time
import wifi as wifi
import ntptime
import machine


def _format_date(date_str):
    parts = date_str.split('.')
    
    # Prüfen, ob ein Jahr im String vorhanden ist (z.B. "28.5.2026")
    if len(parts) >= 3 and parts[2].strip():
        jahr = int(parts[2])
    else:
        # Fallback: Wenn nur "28.5." übergeben wird, nimm das aktuelle Jahr der Systemuhr
        jahr = time.localtime()[0]
        
    return "{:04d}{:02d}{:02d}".format(jahr, int(parts[1]), int(parts[0]))

async def _get_csv_value(date_str, stunde, filename, col_idx):
    target_date = _format_date(date_str)
    target_stunde = str(stunde)
    filepath = "plan_files/" + filename + ".csv"
    
    with open(filepath, "r") as f:
        next(f) # Die erste Zeile (Header) überspringen
        
        for line in f:
            parts = line.strip().split(";")
            
            if parts[0] == target_date and parts[1] == target_stunde:
                if len(parts) > col_idx:
                    return parts[col_idx]
                return ""
            
            # Gibt die Kontrolle kurz an den Scheduler zurück, 
            # damit das Durchsuchen der CSV den ESP32 nicht blockiert.
            await asyncio.sleep(0) 
            
    return ""

async def get_fach(date_str, stunde, filename):
    return await _get_csv_value(date_str, stunde, filename, 4)

async def get_lehrer(date_str, stunde, filename):
    return await _get_csv_value(date_str, stunde, filename, 5)

async def get_raum(date_str, stunde, filename):
    return await _get_csv_value(date_str, stunde, filename, 6)

async def get_info(date_str, stunde, filename):
    info_text = await _get_csv_value(date_str, stunde, filename, 7)
    
    if info_text.strip():
        return 1
    else:
        return 0
    
datum = {}
        
async def update_week_vars():
    global datum
    try:
        # station = network.WLAN(network.STA_IF)
        # print("connecting...", end="")
        # timeout = 300
        # while not station.isconnected() and timeout > 0:
        #     print(".", end="")
        #     time.sleep(0.1)
        #     timeout -=1
        wifi.connect()
        ntptime.host = "de.pool.ntp.org"
        ntptime.settime() 
        # station = network.WLAN(network.STA_IF)
        # if station.active():
        #     station.disconnect()
        #     station.active(False)
        #     print("WiFi disabled")
        # else:
        #     print("not connected")
        wifi.disconnect()
            
        # Zeitkorrektur (Sommerzeit 2026: UTC+2)
        sec = time.time() + (120 * 60)
        (Y, M, D, HH, MM, SS, WD, YD) = time.localtime(sec)
        machine.RTC().datetime((Y, M, D, 0, HH, MM, SS, 0))
        
        # Kurze Pause für den Scheduler
        await asyncio.sleep(0)

        # 2. Berechnung DIESE Woche
        now_ts = time.time()
        current_weekday = time.localtime(now_ts)[6] # 0=Mo
        monday_akt_ts = now_ts - (current_weekday * 86400)
        
        tage = ["mo", "di", "mi", "do", "fr"]
        
        for i in range(5):
                    t = time.localtime(monday_akt_ts + (i * 86400))
                    datum[tage[i] + "_akt"] = "{}.{}.".format(t[2], t[1])
            
        # 3. Berechnung NÄCHSTE Woche
        monday_nae_ts = monday_akt_ts + (7 * 86400)
        
        for i in range(5):
            t = time.localtime(monday_nae_ts + (i * 86400))
            datum[tage[i] + "_nae"] = "{}.{}.".format(t[2], t[1])
            
        print("datum aktuell")
            
    except Exception as e:
            print("error:", e)