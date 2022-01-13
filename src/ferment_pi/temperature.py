# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import sys
import time
import board
import adafruit_dht


class Temperature:
    def __init__(self, pin=board.D4):
        self.dht_device = adafruit_dht.DHT11(pin)

        print("Temperature init!")

    def read(self):
        try:
            temperature_c = self.dht_device.temperature
            humidity = self.dht_device.humidity
            return {'temperature': temperature_c, 'humidity': humidity}
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            return None
        except Exception as error:
            print("exiting")
            tem.exit()
            raise error

    def exit(self):
        self.dht_device.exit()

# Initial the dht device, with data pin connected to:


# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)


if __name__ == '__main__':
    tem = Temperature(pin=board.D4)

    while True:
        temp_data = tem.read()
        print(
            "Temp: {:.1f} C    Humidity: {}% ".format(
                temp_data['temperature'], temp_data['humidity']
            )
        )

        time.sleep(2.0)
