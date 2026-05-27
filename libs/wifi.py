import network
import utime as time
import libs.secrets as secrets
import uasyncio as asyncio
async def connect():
    station = network.WLAN(network.STA_IF)
    if station.isconnected():
        print("already connected")
        return
    station.active(True)

    station.connect(secrets.wifi_ssid, secrets.wifi_pass)

    print("connecting...", end="")
    timeout = 300
    while not station.isconnected() and timeout > 0:
        print(".", end="")
        await asyncio.sleep(0.1)
        timeout -=1

    print("\nconnected with ip", station.ifconfig()[0])
    
async def disconnect():
    station = network.WLAN(network.STA_IF)
    if station.active():
        station.disconnect()
        station.active(False)
        print("WiFi disabled")
    else:
        print("not connected")