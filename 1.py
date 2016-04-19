#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Fib(object):

    def __init__(self, num):
        a, b ,self.numbers = 0, 1 , []
        for i in range(num):
            self.numbers.append(a)
            a, b = b, a+b
    
    def __len__(self):    
        return len(self.numbers)
        
    def __str__(self):
        return str(self.numbers)
        	
f= Fib(10)
f1 = Fib(20)
print f
print f1
print len(f)
print len(f1)

