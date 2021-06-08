#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 11:03:15 2021

@author: evelynebushuru
"""

import os

def createtextfile():
    newtextfile = open('.gitignore','w')
    for root,directory,filename in os.walk('/Users/evelynebushuru/.spyder-py3'):
        for files in filename:
            if not files.endswith('.py'):
                newtextfile.write(f'{files}\n')
    newtextfile.close()
    newtextfile=open('.gitignore','r')
    if newtextfile.mode =='r':
        contents=newtextfile.read()
    return print(contents)

createtextfile()
