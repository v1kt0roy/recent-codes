# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:55:58 2021

@author: 0
"""

from PIL import Image, ImageOps
def add_border(img_file):
    image = Image.open('setu/'+img_file)
    image = ImageOps.expand(image, border=10, fill=0)
    image.save("image/"+img_file)
