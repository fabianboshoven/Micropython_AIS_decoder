# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()
import network

# Set up WiFi credentials
WIFI_SSID = ""
WIFI_PASSWORD = ""

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASSWORD)

# Wait until the connection is established
while not wlan.isconnected():
    pass

# Print the IP address
print("Connected to WiFi with IP address:", wlan.ifconfig()[0])
