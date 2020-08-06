# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:04:43 2020

@author: user
"""

import os.path
if os.path.isfile("file.txt"):
    print('檔案存在')
else:
    print('檔案不存在')

fo=open('file.txt','w')
fo.write('hello')
fo=open('file.txt','r')
fo.read()
fo=open('file.txt','a')
fo.write('?')
fo.close()