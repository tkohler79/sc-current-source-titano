import time
import board
import digitalio
from adafruit_pyportal import PyPortal

# Set up where we'll be fetching data from
DATA_SOURCE = "https://www.adafruit.com/api/quotes.php"
QUOTE_LOCATION = [0, 'text']
AUTHOR_LOCATION = [0, 'author']

# the current working directory (where this file is)
cwd = ("/"+__file__).rsplit('/', 1)[0]
pyportal = PyPortal(url=DATA_SOURCE,
                    json_path=(QUOTE_LOCATION, AUTHOR_LOCATION),
                    status_neopixel=board.NEOPIXEL,
                    default_bg=cwd+"/quote_background.bmp",
                    text_font=cwd+"/fonts/Arial-ItalicMT-23.bdf",
                    text_position=((20, 160),  # quote location
                                   (5, 280)), # author location
                    text_color=(0xFFFFFF,  # quote text color
                                0x8080FF), # author text color
                    text_wrap=(40, # characters to wrap for quote
                               0), # no wrap for author
                    text_maxlen=(180, 30), # max text size for quote & author
                   )

# speed up projects with lots of text by preloading the font!
pyportal.preload_font()

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT
while True:
    try:
        value = pyportal.fetch()
        print("Response is", value)
    except (ValueError, RuntimeError) as e:
        print("Some error occured, retrying! -", e)
    led.value = True
    print(led.value)
    time.sleep(60)
