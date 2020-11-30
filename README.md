# Repo for pyportal titano code that will be used for controlling 8 channel current source
##  Description of folders:
-  adafruit-circuitpython-bundle-6.x-mpy-20201126:  has circuit python 6 libraries that correspond to uf2 file
- titano_cpy_v5:  files from titano board that worked with v5 of circuit python
- titano_cpy_v6:  files from titano board that worked wtih v6 of circuit python

## Things to do
* Add python code to set current by talking to DAC chip... Difficulty level:  easy
*  write to DAC.txt file on SD card everytime DAC values are changed... Difficulty level: medium
*  On boot check if DAC.txt file exists on SD card, if not create it.  Difficulty level: medium
*  Add on/off button for all channels of the current source... Difficulty level: hard

