# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 02:05:24 2022

@author: Aadil
"""

#this is a differential calculator - or at least an attempt
#currently it can only do 1digit,1variable and a 1digit power


def Diff():
    x=input("input a number e.g.: 2x^2: ")
    y=list(x)
    z=[]
    yz=""
    for i in y:
        try:
            z.append(int(i))
        except:
            z.append(i)
    for i in z[1:-1]:
        yz+=(str(i)) 
    xy=str(z[-1]*z[0])+yz+str(z[-1]-1)
    print(xy)
    return

Diff()
