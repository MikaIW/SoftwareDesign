# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 20:47:29 2014

@author: mwelches
"""

# Exercise 3-5 from Think Python

a = '+' + 4*'-'
b = '|' + 4*' '

def drawlines4:
    print 2*a + '+'
    print 2*b + '|'
    print 2*b + '|'
    print 2*b + '|'
    print 2*b + '|'
    

def drawgrid:
    drawlines4
    drawlines4
    print 2*a + '+'
