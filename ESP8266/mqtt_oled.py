#
# A MicroPython script for an Adafruit Feather Huzzah
# with an attached Feather OLED display (using I2C)
# Requires the ssd1306 library
#

from umqtt.simple import MQTTClient
import utime
from machine import Pin
import oled_message_display
import wifi_connection

last_messages = {}
       
def mqtt_message_received(topic, msg):
    # add or update the latest stored message for this topic
    last_messages[topic] = msg
    # and display it on the screen
    oled_message_display.show_message(topic, msg)

def show_message_with_idx(msg_to_show):
    if len(last_messages) == 0:
        return
    try:
        idx = 0
        for topic, msg in last_messages.items():
            if idx == msg_to_show:
                oled_message_display.show_message(topic, msg)
                break
            idx = idx + 1
    except:
        oled_message_display.show_message("error", "error")


# Connect to wifi
wifi_connection.setup_wifi()

# Show an initial message
oled_message_display.show_message("Waiting for","messages...")

# Setup up MQTT
c = MQTTClient("umqtt_client", "192.168.1.16",port=1883)
c.set_callback(mqtt_message_received)
c.connect()
c.subscribe("Home/#")

# B-button on the Feather OLED is connected to
# pin 16 on the Feather Huzzah board
button_B = Pin(16, Pin.IN) 

#
# Poll for messages and check if the B-button is pressed
# (if pressed, the next topic's message should be shown)
#
msg_to_show=0
while 1:
    if button_B.value() == 0:
        msg_to_show = msg_to_show + 1
        if msg_to_show > len(last_messages):
            msg_to_show = 0
        show_message_with_idx(msg_to_show)

    try:
        c.check_msg()
    finally:
        utime.sleep(0.5)

c.disconnect()
