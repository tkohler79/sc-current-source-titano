
# These pins are used as both analog and digital! XL, XR and YU must be analog
# and digital capable. YD just need to be digital
ts = adafruit_touchscreen.Touchscreen(board.TOUCH_XL, board.TOUCH_XR,
                                      board.TOUCH_YD, board.TOUCH_YU,
                                      calibration=((5200, 59000), (5800, 57000)),
                                      z_threshhold = 25000,
                                      samples = 1,
                                      size=(480, 320))

# the current working directory (where this file is)
cwd = ("/"+__file__).rsplit('/', 1)[0]
fonts = [file for file in os.listdir(cwd+"/fonts/")
         if (file.endswith(".bdf") and not file.startswith("._"))]
for i, filename in enumerate(fonts):
    fonts[i] = cwd+"/fonts/"+filename
print(fonts)
# THE_FONT = "/fonts/Arial-12.bdf"
# THE_FONT = "/fonts/Helvetica-bold-16.bdf"
# THE_FONT = "/fonts/Arial-ItalicMT-23.bdf"
THE_FONT = "/fonts/Ubuntu-Medium-24.bdf"
DISPLAY_STRING = "Button Text"

# Make the display context
splash = displayio.Group(max_size=20)
board.DISPLAY.show(splash)
BUTTON_WIDTH = 140
BUTTON_HEIGHT = 60
BUTTON_MARGIN = 15

##########################################################################
# Make a background color fill

color_bitmap = displayio.Bitmap(480, 320, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x404040
bg_sprite = displayio.TileGrid(color_bitmap,
                               pixel_shader=color_palette,
                               x=0, y=0)
print(bg_sprite.x, bg_sprite.y)
splash.append(bg_sprite)

##########################################################################

# Load the font
font = bitmap_font.load_font(THE_FONT)

buttons = []

for i in range(8):
    button = Button(x=BUTTON_MARGIN*(i//4+1)+BUTTON_WIDTH*(i//4),
                    y=BUTTON_MARGIN*(i%4+1)+BUTTON_HEIGHT*(i%4),
                      width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                    label_color = 0x00FF00, selected_label = 0x00FF00,
                      label="%f"%values[i], label_font=font, style=Button.SHADOWROUNDRECT)
    buttons.append(button)
button = Button(x=BUTTON_MARGIN*(3)+BUTTON_WIDTH*(2),
                y=BUTTON_MARGIN*(1)+BUTTON_HEIGHT*(0),
                  width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                  label="<<<", label_font=font, style=Button.SHADOWROUNDRECT)
buttons.append(button)
button = Button(x=BUTTON_MARGIN*(3)+BUTTON_WIDTH*(2),
                y=BUTTON_MARGIN*(2)+BUTTON_HEIGHT*(1),
                  width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                  label="+", label_font=font, style=Button.SHADOWROUNDRECT)
buttons.append(button)
button = Button(x=BUTTON_MARGIN*(3)+BUTTON_WIDTH*(2),
                y=BUTTON_MARGIN*(3)+BUTTON_HEIGHT*(2),
                  width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                  label="-", label_font=font, style=Button.SHADOWROUNDRECT)
buttons.append(button)
button = Button(x=BUTTON_MARGIN*(3)+BUTTON_WIDTH*(2),
                y=BUTTON_MARGIN*(4)+BUTTON_HEIGHT*(3),
                  width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                  label=">>>", label_font=font, style=Button.SHADOWROUNDRECT)
buttons.append(button)


for b in buttons:
    splash.append(b.group)

if True:
    p = ts.touch_point
    if p:
        print(p)
        for i, b in enumerate(buttons):
            if b.contains(p):
                # print("Button %d pressed" % i)
                if i<8 :
                    b.selected = True
                    if (last_selected >= 0) and (i != last_selected):
                        buttons[last_selected].selected = False
                    last_selected = i
                else:
                    b.selected = True
                    if (last_op >= 0) and (last_op != i):
                        buttons[last_op].selected = False
                    last_op = i
                    now = time.time()
                    #  Do operation
                    if i==8:
                        step = step * 10
                        if step>0.1:
                            step = 0.1
                    elif i==11:
                        step = step / 10
                        if step<0.0001:
                            step = 0.0001
                    elif i==9:
                        if last_selected>=0:
                            values[last_selected] += step
                            values[last_selected] = round(values[last_selected],6)

                            set_dac(last_selected, values[last_selected])
                    elif i==10:
                        if last_selected>=0:
                            values[last_selected] -= step
                            values[last_selected] = round(values[last_selected],6)
                            set_dac(last_selected, values[last_selected])
                    last_op_time = now

    else:
        now = time.time()
        # print('last_op: %d'%last_op)
        if (now-last_op_time) > 0.001:
            buttons[last_op].selected = False

            # else:
            #     print('no button')
            #     for i in range(8,12):
            #         buttons[i].selected = False

