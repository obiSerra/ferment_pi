import time
import RPi.GPIO as GPIO
import datetime

from screen import Screen
from temperature import Temperature


def run_app():
    screen = Screen()
    temp = Temperature()
    screen.draw_text('FermentPi', position=(30, 20))
    screen.render()
    time.sleep(2)

    time.sleep(2)
    try:
        while True:
            temp_data = temp.read()
            if temp_data is not None:
                message = "Temp: {:.1f} C \nHumidity: {}% ".format(
                    temp_data['temperature'], temp_data['humidity']
                )
                now = datetime.datetime.now()
                print(message)
                screen.new_screen()
                screen.draw_text(message, font_size=10)
                screen.draw_text("time: {}".format(now), font_size=8,
                                 position=(0, 50))

                screen.render()

            time.sleep(2)
    except KeyboardInterrupt:
        temp.exit()
        print("ctrl + c:")
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    run_app()
