#!/usr/bin/env python3

import signal
from  sh1106 import SH1106
import time
from sh1106 import config

from PIL import Image,ImageDraw,ImageFont

FONT_DIR='assets'

class Screen():

    def __init__(self):
        self.disp = SH1106.SH1106()
        # Initialize library.
        self.disp.Init()
        # Clear display.
        self.disp.clear()
        self.image = None

    @property
    def width(self):
        return self.disp.width
    
    @property
    def height(self):
        return self.disp.height
        
    def new_screen(self, bg_color=1):
        self.image = Image.new('1', (self.disp.width, self.disp.height), bg_color)

    def render(self):
        self.disp.ShowImage(self.disp.getbuffer(self.image))
        time.sleep(1)

    def draw_border(self, top=True, bottom=True, left=True, right=True, fill=0):
        draw = ImageDraw.Draw(self.image)
        if top:
            draw.line([(0,0),(127,0)], fill = fill)
        if left:
            draw.line([(0,0),(0,63)], fill = fill)
        if bottom:
            draw.line([(0,63),(127,63)], fill = fill)
        if right:
            draw.line([(127,0),(127,63)], fill = fill)

    def draw_text(self, text, font_size=13, position=(0, 0), font='Font.ttf', bg_color=1, fill=0):
        if not self.image:
            self.new_screen(bg_color)
        draw = ImageDraw.Draw(self.image)    
        font = ImageFont.truetype('{}/{}'.format(FONT_DIR, font), font_size)
        draw.text(position, text, font = font, fill = fill)


def quit_gracefully(*args):
    #epdconfig.module_exit()
    exit()

signal.signal(signal.SIGINT, quit_gracefully)

if __name__ == '__main__':
    try:
        display = Screen()
        display.draw_text('Hello world oooo')
        display.draw_border()
        display.render()

    except IOError as e:
        print(e)
        
    except KeyboardInterrupt:    
        print("ctrl + c:")
        quit_gracefully()
