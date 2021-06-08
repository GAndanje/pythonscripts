#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 23:08:59 2021

@author: evelynebushuru
"""

def threelargestNums(array):
    listoflargestThree =[None]*3
    for num in  array:
        updatelargestnum(num,listoflargestThree)
    return listoflargestThree

def updatelargestnum(num,array):
    if array[2]== None or num > array[2]:
        updatelist(array,num,2)
    elif array[1]== None or num > array[1]:
        updatelist(array,num,1)
    elif array[0]==None or num > array[0]:
        updatelist(array,num,0)
        
def updatelist(array,num,idx):
    for i in range(idx+1):
        if i == idx:
            array[i]= num
        else:
            array[i]=array[i+1]
            
print(threelargestNums([1,2,4,5,9,3,6,5,10,20,30]))
