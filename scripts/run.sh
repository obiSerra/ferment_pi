#!/bin/bash

cd /home/pi/fermentpi/ && docker-compose up -d

python3 /home/pi/fermentpi/src/ferment_pi/main.py