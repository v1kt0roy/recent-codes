# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:21:54 2021

@author: 0
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 09:02:00 2020

@author: V1kt0r
"""

def get_image(url):
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    socket.setdefaulttimeout(180)
    file_name='1.jpg'
    image_name=os.getcwd()+"/"+file_name
    if os.path.isfile(os.getcwd()+"/"+file_name)==False:
        try:
            urllib.request.urlretrieve(url,filename=image_name)
        except socket.timeout:
            count = 1
            while count <= 5:
                try:
                    urllib.request.urlretrieve(url,filename=image_name)                                                
                    break
                except socket.timeout:
                    err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
                    print(err_info)
                    count += 1
            if count > 5:
                print("downloading picture fialed!")
    
    return
import requests  
import random
import socket
import re
import urllib
import os.path
import configparser

