# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 15:01:27 2019

@author: korne
"""

import datetime

def hello_world():
    print('hello world!')
    now = datetime.datetime.now()
    print('it is {}'.format(now))

if __name__ == "__main__":
    hello_world()
    
import tacoworld.py