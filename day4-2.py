# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:58:57 2020

@author: user
"""

file=open('Penguins.jpg','rb')
img=file.read()
file.close()

file=open('copy.jpg','wb')
file.write(img)
file.close()
