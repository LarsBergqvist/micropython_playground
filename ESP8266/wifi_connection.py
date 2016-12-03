import network
import utime

def setup_wifi():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    # Replace with your SSID and WiFi password
    sta_if.connect('SSID', 'PASSWORD')
    while not sta_if.isconnected():
        utime.sleep(1)