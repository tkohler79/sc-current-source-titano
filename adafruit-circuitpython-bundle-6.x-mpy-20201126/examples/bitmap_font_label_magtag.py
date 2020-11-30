"""
This example uses addfruit_display_text.label to display text using a custom font
loaded by adafruit_bitmap_font.
Adapted for use on MagTag
"""
import time
import board
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

# use built in display (PyPortal, PyGamer, PyBadge, CLUE, etc.)
# see guide for setting up external displays (TFT / OLED breakouts, RGB matrices, etc.)
# https://learn.adafruit.com/circuitpython-display-support-using-displayio/display-and-display-bus
display = board.DISPLAY
# wait until we can refresh the display
time.sleep(display.time_to_refresh)

# Set text, font, and color
text = "HELLO WORLD\nbitmap_font example"
font = bitmap_font.load_font("fonts/Arial-16.bdf")
color = 0xFFFFFF
background_color = 0x999999

# Create the tet label
text_area = label.Label(
    font,
    text=text,
    color=color,
    background_color=background_color,
    padding_top=3,
    padding_bottom=3,
    padding_right=4,
    padding_left=4,
)
text_area.line_spacing = 1.0
# Set the location
text_area.x = 20
text_area.y = 20

# Show it and refresh
display.show(text_area)
display.refresh()
while True:
    pass
