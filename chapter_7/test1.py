#-*-coding:utf-8-*-

import tesserocr
from PIL import Image
# import locale
# locale.setlocale(locale.LC_ALL,"C")

image = Image.open("img.jpg")

result = tesserocr.image_to_text(image)
print(result)
# import tesserocr
#
# print(tesserocr.file_to_text('image.jpg'))