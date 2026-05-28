import uasyncio as asyncio
import gc
import os


headers = {
    "User-Agent": "Mozilla/5.0",
    "Host": "plan-files.schulische-dinge.de"
}
base_url = "http://plan-files.schulische-dinge.de/klassen/"
index_url = "http://plan-files.schulische-dinge.de/klassen/index.txt"
index_loc = "index.txt"

async def download_index():
    try:
        reader, writer = await asyncio.open_connection(headers["Host"], 80)
        
        request = f"GET /klassen/index.txt HTTP/1.1\r\nHost: {headers['Host']}\r\nUser-Agent: {headers['User-Agent']}\r\nConnection: close\r\n\r\n"
        writer.write(request.encode('utf-8'))
        await writer.drain()

        status_line = await reader.readline()
        if not status_line:
            print("Keine Antwort vom Server erhalten.")
            writer.close()
            await writer.wait_closed()
            return

        status_code = int(status_line.split()[1])
        
        # Header überspringen
        while True:
            line = await reader.readline()
            if line == b"\r\n" or line == b"" or not line:
                break

        if status_code == 200:
            i = open(index_loc, "w")
            while True:
                line = await reader.readline()
                if not line: # Wenn Verbindung zu Ende oder leer
                    break
                i.write(line.decode('utf-8'))
            print("Index download completed with status code", status_code)
            i.close()
        else:
            print("Index download failed with status code:", status_code)
            
        writer.close()
        await writer.wait_closed()
    except Exception as e:
        print("Fehler beim Index-Download:", e)

async def download_plan_files():
    print("Plan File Downlaod starting")
    try:
        index_file = open(index_loc, "r")
    except OSError:
        print("Index-Datei existiert nicht!")
        return

    for line in index_file:
        name = line.strip()
        if not name:
            continue
            
        full_url = base_url + name
        print("Downloading file from", full_url)
        
        try:
            reader, writer = await asyncio.open_connection(headers["Host"], 80)
            
            request = f"GET /klassen/{name} HTTP/1.1\r\nHost: {headers['Host']}\r\nUser-Agent: {headers['User-Agent']}\r\nConnection: close\r\n\r\n"
            writer.write(request.encode('utf-8'))
            await writer.drain()

            status_line = await reader.readline()
            if not status_line:
                print(f"Keine Antwort für {name} erhalten.")
                writer.close()
                await writer.wait_closed()
                continue

            status_code = int(status_line.split()[1])
            print("Status code:", status_code)
            
            while True:
                line = await reader.readline()
                if line == b"\r\n" or line == b"" or not line:
                    break

            if status_code == 200:
                f = open(name, "wb")
                while True:
                    chunk = await reader.read(256)
                    if not chunk or chunk == b"":
                        break
                    f.write(chunk)
                f.close()
                
            writer.close()
            await writer.wait_closed()
        except Exception as e:
            print(f"Fehler bei Datei {name}: {e}")
            
        gc.collect()
        
    index_file.close()

    try:
        pf = open("05-01.csv")
        print(pf.read())
        pf.close()
    except OSError:
        print("Testdatei 05-01.csv konnte nicht geoeffnet werden.")

async def download():
    await download_index()
    await download_plan_files()

async def list_files():
    files = os.listdir()
    print(files)
        
async def rem_files():
    for file in os.listdir():
        if file.endswith(".csv"):
            try:
                os.remove(file)
                print(f"Datei {file} wurde geloescht.")
            except OSError:
                print("Datei", file, "konnte nicht geloescht werden!")
