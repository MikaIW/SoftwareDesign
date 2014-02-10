# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:04:15 2014

@author: mwelches
"""

# Fermat's Theorem: There are no integers a, b, and c such that a^n + b^n = c^n.
# Example 5-3 from Think Python: takes four parameters - a, b, c and n - and checks to see if Fermat's theorem holds.

def check_fermat(a,b,c,n):
    if n > 2 and a^n + b^n == c^n:
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."
        
def check_fermat2(a,b,c,n):
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
    check_fermat(a,b,c,n)
