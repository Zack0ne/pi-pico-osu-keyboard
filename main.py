import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
usb_keyboard = Keyboard(usb_hid.devices)

def set_button(x):
    button = digitalio.DigitalInOut(x)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
    return(button)


pin = [board.GP8, board.GP7, board.GP9, board.GP4, board.GP14, board.GP13, board.GP12, board.GP11,  board.GP10, board.GP2, board.GP0, board.GP6]
key = [Keycode.ONE, Keycode.TWO, Keycode.GRAVE_ACCENT, Keycode.ESCAPE, Keycode.A, Keycode.S, Keycode.SPACE, Keycode.K, Keycode.L, Keycode.F2, Keycode.F12, Keycode.THREE]
"""
pin = [board.GP8, board.GP7, board.GP9, board.GP4]
key = [Keycode.ONE, Keycode.TWO, Keycode.GRAVE_ACCENT, Keycode.ESCAPE]
"""
all_key = list(map(lambda x : set_button(x), pin))
last_value = list(map(lambda x : x.value, all_key))

"""
import time
loop_test = 10000
start = time.time()
x = 0
while x < loop_test: #second test
    x = x + 1
    for i, button in enumerate(all_key):
        if last_value[i] != button.value:
            last_value[i] = button.value
            if not button.value:
                usb_keyboard.press(key[i])
            else:
                usb_keyboard.release(key[i])
print("Loop frequency : {}".format(str(loop_test / (time.time() - start))))
"""
while True:
    for i, button in enumerate(all_key):
        if last_value[i] != button.value:
            last_value[i] = button.value
            if button.value:
                usb_keyboard.release(key[i])
            else:
                usb_keyboard.press(key[i])