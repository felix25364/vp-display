
import urequests
import network
import utime as time
import gc
import machine
import os
import libs.wifi as wifi

station = network.WLAN(network.STA_IF)
station.active(True)

headers = {
    "User-Agent": "Mozilla/5.0",
    "Host": "plan-files.schulische-dinge.de"
}
base_url = "http://plan-files.schulische-dinge.de/klassen/"
index_url = "http://plan-files.schulische-dinge.de/klassen/index.txt"
index_loc = "index.txt"

wifi.connect()

print("Available ram:", gc.mem_free())

def download_index():
    index = urequests.get(index_url, headers=headers)

    if index.status_code == 200:
        i = open(index_loc, "w")
        i.write(index.text)
        print("Index download completed with status code", index.status_code)
        i.close()
        index.close()
    else:
        print("Index download failed with status code:", index.status_code)
    
download_index()    

def download_plan_files():
    print("Plan File Downlaod starting")
    index_file = open(index_loc, "r")

    for line in index_file:
        name = line.strip()
        full_url = base_url + name
        res = urequests.get(full_url)   
        print("Downloading file from", full_url)
        print("Status code:", res.status_code)
        print("Available ram:", gc.mem_free())
        f = open(name, "wb")
        f.write(res.content)
        f.close()
        res.close()
        gc.collect()
        print("Available ram after gc:", gc.mem_free())
    index_file.close()


    pf = open("05-01.csv")
    print(pf.read())

download_plan_files()

def list_files():
        files = os.listdir()
        print(files)
        
def rem_files():
        for file in os.listdir():
            if file.endswith(".csv"):
                try:
                    os.remove(file)
                    print(f"Datei {file} wurde geloescht.")
                except OSError:
                    print("Datei", file, "konnte nicht geloescht werden!")