import machine
i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
import ssd1306
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

def show_message(topic,msg):
    topic_line1 = str(topic,"utf-8")
    topic_line2 = ""

    parts=topic_line1.split("/")
    if len(parts) == 3:
        topic_line1 = parts[1]
        topic_line2 = parts[2]

    oled.fill(0)
    oled.text(topic_line1, 0, 0)
    oled.text(topic_line2, 0, 10)
    oled.text(msg, 0, 20)
    oled.show()
