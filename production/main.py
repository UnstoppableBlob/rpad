# pinmap:
# GPIO6/SDA: 0.91' OLED (SSD1306) and IO expander (MCP23017)
# GPIO7/SCL: 0.91' OLED (SSD1306) and IO expander (MCP23017)
# GPB0 & GPB1: Rotary Encoder 1
# GPB2: Rotary Encoder 1 (push button)
# GPB3 & GPB4: Rotary Encoder 2
# GPB5: Rotary Encoder 2 (push button)
# GPB6 & GPB7, and GPA0 to GPA6: 9 push buttons

# actions:
# rotary encoder 1: screen brightness
# rotary encoder 2: volume
# push buttons: 
# - email macro, phone macro, address macro
# - play/pause, previous track, next track
# - alt+tab, alt+shift+tab, alt+f4
# OLED shows brightness, volume, and time

# I have no way to test this without having the actual parts so hopefully it mostly works? the rotary encoders and IO expander parts are incomplete so it wouldn't work yet anyway
import board
import busio
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.extensions.media_keys import MediaKeys
import adafruit_ssd1306
# not sure how to use rotary encoders yet


keyboard = KMKKeyboard()
macros = Macros()
media_keys = MediaKeys()
keyboard.modules.append(macros)
keyboard.extensions.append(media_keys)

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)


oled.fill(0)
oled.show()

brightness = 50
volume = 50


def showOLED():
    oled.fill(0)
    
    current_time = time.monotonic()
    time_str = f"{int(current_time//60):02d}:{int(current_time%60):02d}"
    
    oled.text(f"Bright: {brightness}%", 0, 0, 1)
    oled.text(f"Volume: {volume}%", 0, 10, 1)
    oled.text(f"Time: {time_str}", 0, 20, 1)
    oled.show()


def brightness_encoder():
    global brightness
    # figure out how to actually set computer brightness
    showOLED()


def volume_encoder():
    global volume
    # figure out how to actually set computer volume
    showOLED()


PINS = # TODO add the pins from the IO expander

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)


keyboard.keymap = [
    [
        KC.MACRO("Email"), KC.MACRO("Phone"), KC.MACRO("Address"),
        KC.MEDIA_PLAY_PAUSE, KC.MEDIA_PREV_TRACK, KC.MEDIA_NEXT_TRACK,
        KC.LALT(KC.TAB), KC.LALT(KC.LSHIFT(KC.TAB)), KC.LALT(KC.F4)
    ]
]

if __name__ == '__main__':
    keyboard.go()