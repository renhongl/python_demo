

# coding: utf-8


# Create a image


from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def get_rnd_color():
	return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def get_rnd_code(n):
	code = ''
	for i in range(n):
		code = code + str(chr(random.randint(65, 90)))
	return code

width, height = 150, 50

image = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(image)

for i in range(width):
	for j in range(height):
		draw.point((i, j), get_rnd_color())

font = ImageFont.truetype('arial.ttf', 25)

draw.text((10, 10), get_rnd_code(7), fill=(255, 255, 255, 1), font=font)
# image = image.filter(ImageFilter.BLUR)


image.save('./code.png')


