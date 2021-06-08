#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:55:48 2021

@author: evelynebushuru
"""


def smallestarrayNum(array):
    smallestnumIdx = 0
    smallestnum = array[0]
    while smallestnumIdx < len(array)-1:
        if array[smallestnumIdx+1]< smallestnum:
            smallestnum = array[smallestnumIdx+1]
            smallestnumIdx += 1
        else:
            smallestnumIdx += 1
    return smallestnum
print(smallestarrayNum([3,4,1,-1.,5,-3,22,4-3]))