

#windows下，只需要安装Tesseract，以及pytesseract库，即可识别验证码

from PIL import Image
import pytesseract


image = Image.open('./input/1-22.jpg')
code = pytesseract.image_to_string(image)
print(code)

