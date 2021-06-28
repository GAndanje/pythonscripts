#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 13:10:11 2021

@author: evelynebushuru
"""

def recurssivePall(string):
    string =''.join(string.split()).lower()
    print(string) #just a debugger
    if len(string) <=1:
        return True
    else:
        return string[0]==string[-1] and recurssivePall(string[1:-1])


print('this is recurssive on pallindrome 999')
print(recurssivePall("9"))
print('this is recurssive on pallindrome 969')
print(recurssivePall("969"))
print('this is recurssive on pallindrome 975')
print(recurssivePall("975"))
print('this is recurssive on pallindrome 9678')
print(recurssivePall("9678"))
print('this is recurssive on pallindrome "huraa"')
print(recurssivePall("huraa"))
print('this is recurssive on pallindrome "racecar"')
print(recurssivePall("racecar"))
print('this is recurssive on pallindrome "Was it a car or a cat I saw"')
print(recurssivePall("Was it a car or a cat I saw"))
print('this is recurssive on pallindrome "Murder for a jar of red rum"')
print(recurssivePall("Murder for a jar of red rum"))


def iterativePall(string):
    string1 = ''.join(string.lower().split())
    print(string1)
    leftpointer=0
    rightpointer =len(string1)-1
    while leftpointer <rightpointer:
        if string1[leftpointer]==string1[rightpointer]:
            leftpointer += 1
            rightpointer -= 1
        else:
            return False
    return True


print('this is iterative on pallindrome 999')
print(iterativePall("999"))
print('this is iterative on pallindrome 969')
print(iterativePall("969"))
print('this is iterative on pallindrome 975')
print(iterativePall("975"))
print('this is iterative on pallindrome 9678')
print(iterativePall("9678"))
print('this is iterative on pallindrome "huraa"')
print(iterativePall("huraa"))
print('this is iterative on pallindrome "racecar"')
print(iterativePall("racecar"))
print('this is iterative on pallindrome "Was it a car or a cat I saw"')
print(iterativePall("Was it a car or a cat I saw"))
print('this is iterative on pallindrome "Murder for a jar of red rum"')
print(iterativePall("Murder for a jar of red rum"))


