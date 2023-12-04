from machine import Pin, I2C
import gc9a01_i2c

# initialize the I2C bus
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)

# create a GC9A01 object
display = gc9a01_i2c.GC9A01_I2C(i2c, width=240, height=240, addr=0x5c)

# set the display orientation
display.rotation(1)

# set the font size and color
font_size = 24
font_color = gc9a01_i2c.Color.WHITE

# create a text string
text = "Hello, world!"

# calculate the text width and height
text_width = display.text_width(text, font_size)
text_height = display.text_height(font_size)

# calculate the center position of the text
center_x = (display.width - text_width) // 2
center_y = (display.height - text_height) // 2

# draw the text on the display
display.text(text, center_x, center_y, font_size, font_color)

# update the display
display.show()

