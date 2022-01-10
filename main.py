import RPi.GPIO as GPIO
import time
from screen import Screen
from keyboard import Keyboard
from datetime import datetime

import threading

pos = [0, 0]

def go_right():
    print("right")
    pos[0] += 1

def go_left():
    print("left")
    pos[0] -= 1

def go_down():
    print("DOWN")
    pos[1] += 1

def go_up():
    print("UP")
    pos[1] -= 1

if __name__ == '__main__':
    try:
        screen = Screen()
        screen.draw_text('welcome!!!')
        screen.draw_border()
        screen.render()
        time.sleep(2)

        pos = [0, 0]

        keyboard = Keyboard(on_click_actions={'up': go_up, 'down': go_down, 'left': go_left, 'right': go_right, 'center': lambda: print("OIOIOIOIOIOI")})
        
        last_frame = datetime.now()

        def render_screen():
            screen.new_screen()
            screen.draw_text('obi', position=pos)
            screen.draw_border()
            screen.render()
        
        while True:
            keyboard.update()
            current_frame = datetime.now()
            delta_t = current_frame - last_frame
            if delta_t.total_seconds() > 1:
                th = threading.Thread(target=render_screen)
                th.start()
                last_frame = current_frame
                

    except IOError as e:
        print(e)
        
    except KeyboardInterrupt:    
        print("ctrl + c:")
    finally:
        GPIO.cleanup()
