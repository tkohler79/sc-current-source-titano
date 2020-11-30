import os
import busio
import digitalio
import board
import storage
import adafruit_sdcard

# See if a card is present
card_detect_pin = digitalio.DigitalInOut(board.SD_CARD_DETECT)
card_detect_pin.direction = digitalio.Direction.INPUT
card_detect_pin.pull = digitalio.Pull.UP
print('SD card present: %s' % card_detect_pin.value)


# blink led
import digitalio
import board
import time

led = digitalio.DigitalInOut(board.L)  # Or board.D13
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)


# CircuitPython demo - I2C scan

import time
import board
import busio

i2c = busio.I2C(board.SCL, board.SDA)

while not i2c.try_lock():
    pass

while True:
    print("I2C addresses found:", [hex(device_address)
                                   for device_address in i2c.scan()])
    time.sleep(2)

