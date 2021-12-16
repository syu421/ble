SSID = ["SSID"]
PASS = ["Password"]

import utime
import network
import webrepl


def connect_wifi(ssid, password):
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)

    for configuration in zip(SSID, PASS):
        print("TRY: ssid:" + configuration[0] + " pass:" + configuration[1])
    
        wifi.connect(configuration[0], configuration[1])
        timeout=10
        while not wifi.isconnected() and timeout > 0:
            print("TIME: " + str(timeout))
            utime.sleep(1)
            timeout -= 1
    
        if wifi.isconnected():
            print("CONNECT: ssid:" + configuration[0] + " pass:" + configuration[1])
            webrepl.start(password="tut2021")
            return wifi
        else:
            print("ERR: ssid:" + configuration[0] + " pass:" + configuration[1])

connect_wifi(SSID,PASS)
