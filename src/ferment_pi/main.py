import time
import RPi.GPIO as GPIO
import datetime

from screen import Screen
from temperature import Temperature
from database import save_temperature


def run_app():
    screen = Screen()
    temp = Temperature()
    screen.draw_text('FermentPi', position=(30, 20))
    screen.render()
    time.sleep(2)

    save_every = 30 * 20
    from_last_save = save_every

    try:
        temp_data = None
        while True:
            from_last_save += 1
            temp_data = temp.read()
            if temp_data is not None:

                temperature = temp_data['temperature']
                humidity = temp_data['humidity']

                if from_last_save > save_every:
                    print('Saving')
                    try:
                        save_temperature(temperature, humidity)
                        from_last_save = 0
                    except Exception as err:
                        print("ERROR in db", err)

                message = "Temp: {:.1f} C \nHumidity: {}% ".format(
                    temperature, humidity
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
