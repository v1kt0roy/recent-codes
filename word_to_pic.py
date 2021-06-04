# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:19:17 2021

@author: 0
"""


from PIL import Image,ImageFont,ImageDraw
import configparser
import os

import re

LINE_CHAR_COUNT = 50*2  # 每行字符数：30个中文字符(=60英文字符)
CHAR_SIZE = 30
TABLE_WIDTH = 4

def line_break(line):
    ret = ''
    width = 0
    for c in line:
        if len(c.encode('utf8')) == 3:  # 中文
            if LINE_CHAR_COUNT == width + 1:  # 剩余位置不够一个汉字
                width = 2
                ret += '\n' + c
            else: # 中文宽度加2，注意换行边界
                width += 2
                ret += c
        else:
            if c == '\t':
                space_c = TABLE_WIDTH - width % TABLE_WIDTH  # 已有长度对TABLE_WIDTH取余
                ret += ' ' * space_c
                width += space_c
            elif c == '\n':
                width = 0
                ret += c
            else:
                width += 1
                ret += c
        if width >= LINE_CHAR_COUNT:
            ret += '\n'
            width = 0
    if ret.endswith('\n'):
        return ret
    return ret + '\n'


cf=configparser.ConfigParser()
cf.read('nanahira.ini',encoding='utf-8')
for a in cf.sections():
    text=cf.get(a,'question') 
    text=line_break(text)
    d_font = ImageFont.truetype('C:/Windows/Fonts/simsun.ttc', CHAR_SIZE)
    lines = text.count('\n')  # 计算行数
    
    image = Image.new("L", (LINE_CHAR_COUNT*CHAR_SIZE // 2, CHAR_SIZE*lines), "white")
    draw_table = ImageDraw.Draw(im=image)
    draw_table.text(xy=(0, 0), text=text, fill='#000000', font= d_font, spacing=4)  # spacing调节机制不清楚如何计算
    
    # image.show()  # 直接显示图片
    image.save(a+'.png')  # 保存在当前路径下，格式为PNG
    image.close()
