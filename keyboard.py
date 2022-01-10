from sh1106 import SH1106
import time
from sh1106 import config
import traceback

import RPi.GPIO as GPIO

import time
import subprocess

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# GPIO define
RST_PIN = 25
CS_PIN = 8
DC_PIN = 24

KEY_UP_PIN = 6
KEY_DOWN_PIN = 19
KEY_LEFT_PIN = 5
KEY_RIGHT_PIN = 26
KEY_PRESS_PIN = 13

KEY1_PIN = 21
KEY2_PIN = 20
KEY3_PIN = 16

GPIO.setmode(GPIO.BCM)

class Button():
    def __init__(self, name, pin, on_click_callback=None, on_release_callback=None, on_pressed_callback=None):
        self.pin = pin
        self.name = name
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.on_click_callback = on_click_callback
        self.on_release_callback = on_release_callback
        self.on_pressed_callback = on_pressed_callback
        self.value = None
        self.last_pressed = None
        self.update()

    def update(self):
        self.last_pressed = self.value
        self.value = not GPIO.input(self.pin)

        if self.on_pressed_callback and self.value:
            self.on_pressed_callback()

        if self.on_click_callback and self.is_pressed:
            self.on_click_callback()
        if self.on_release_callback and self.is_released:
            self.on_release_callback()


    @property
    def is_pressed(self):
        ret = self.value and not self.last_pressed
        return ret

    @property
    def is_released(self):
        ret = not self.value and self.last_pressed
        return ret

    def on_click(self, callback=None):
        self.on_click_callback = callback

    def on_pressed(self, callback=None):
        self.on_pressed_callback = callback

    def on_release(self, callback=None):
        self.on_release_callback = callback

class Keyboard():
    def __init__(self, on_click_actions={}, on_pressed_actions={}):
        self.buttons = {
            'up': {'pin': 6},
            'down': {'pin': 19},
            'left': {'pin': 5},
            'right': {'pin': 26},
            'center': {'pin': 13},
            'key_1': {'pin': 21},
            'key_2': {'pin': 20},
            'key_3': {'pin': 16}
        }

        for b_name in self.buttons:
            btn = self.buttons[b_name]
            self.buttons[b_name]['button'] = Button(b_name, btn['pin'])
            if b_name in on_click_actions:
                self.on_click(b_name, on_click_actions[b_name])
            if b_name in on_pressed_actions:
                self.on_pressed(b_name, on_pressed_actions[b_name])

    def on_click(self, button_name, callback=None):
        if button_name in self.buttons:
            self.buttons[button_name]['button'].on_click(callback)
    def on_pressed(self, button_name, callback=None):
        
        if button_name in self.buttons:
            self.buttons[button_name]['button'].on_pressed(callback)

    def update(self):
        for b_name in self.buttons:
            btn = self.buttons[b_name]['button']
            btn.update()


if __name__ == '__main__':
    try:
        keyboard = Keyboard(on_click_actions={'up': lambda: print("UUUUp"), 'center': lambda: print("center")})
        
        while True:
            keyboard.update()

    except IOError as e:
        print(e)

    except KeyboardInterrupt:
        print("ctrl + c:")
