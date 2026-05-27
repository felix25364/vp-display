# vp-display

A simple MicroPython script for a Waveshare 7" Touch ESP32-S3 display using LVGL to fetch, parse, and display school substitution plans (Vertretungsplan).

## Setup

This project requires a configuration file for your local credentials. Create a file named `secrets.py` in the libs directory of your project:

```python
# secrets.py
WIFI_SSID = "Your_WiFi_Name"
WIFI_PASS = "Your_WiFi_Password"
