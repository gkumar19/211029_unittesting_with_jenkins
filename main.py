#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 16:08:33 2021

@author: hero
"""

def add(a, b):
    return_value = a + b
    return return_value

def subtract(a, b):
    return_value = a - b
    return return_value

def multiply(a, b):
    return_value = a * b
    return return_value

if __name__ != "__main__":
    print('main pipeline is running from other module')

if __name__ == "__main__":
    print('main pipeline is running')