import os
import board
import displayio
import time
from adafruit_bitmap_font import bitmap_font
from adafruit_button import Button
import adafruit_touchscreen
import busio
import digitalio
import storage
import adafruit_sdcard
import supervisor
import json

# See if a card is present
card_detect_pin = digitalio.DigitalInOut(board.SD_CARD_DETECT)
card_detect_pin.direction = digitalio.Direction.INPUT
card_detect_pin.pull = digitalio.Pull.UP
print('SD card present: %s' % card_detect_pin.value)

# Try to connect to the SD card
sdcard = adafruit_sdcard.SDCard(
    busio.SPI(board.SCK, board.MOSI, board.MISO),
    digitalio.DigitalInOut(board.SD_CS)
)

# Mount the card to a directory
virtual_file_system = storage.VfsFat(sdcard)
storage.mount(virtual_file_system, '/sd')

def save_settings(values):
    with open('/sd/DAC.txt','w') as output_file:
        for i in range(8):
            output_file.write('%f\n'%values[i])

values = []
with open('/sd/DAC.txt', 'r') as input_file:
    for i in range(8):
        values.append(float(input_file.readline()))
print('values',values)

def set_dac(index, value):
    # print('set_dac')
    # update hardware

    # update display
    values[index] = value
    # buttons[index].label = '%8.6f' % value
    print('set_dac', index, value)

def check_int(s):
    s = str(s)
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit() 

last_selected = -1
last_op = -1
last_op_time = 0
step = 0.001
while True:
    if supervisor.runtime.serial_bytes_available:
        msg = input()
        msg = msg.strip()
        msg = msg.split()
        if len(msg)<=2 and len(msg)>0:
            command = msg[0]
            if len(msg)==1:
                if command.endswith('?'):
                    #  Need to really check if integer
                    index = int(command[:-1])
                    #  Check if index is in range
                    print('%d %f' % (index, values[index]))
                if command.upper()=='S':
                    save_settings(values)
                if command.upper()=='Z':
                    # set all values to zero
                    for i in range(len(values)):
                        set_dac(i, 0);
                if command.upper()=='R':
                    # set all values to zero
                    for i in range(len(values)):
                        set_dac(i, values[i]);

            else:  # len(msg)==2
                print('command', command, 'value', msg[1])
                if check_int(command):
                    index = int(command)
                    new_value = float(msg[1])
                    set_dac(index, new_value)
                else:
                    print("command", command[:-1], msg[1:])

