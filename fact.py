#!/bin/bash/env python

def factorial(n):
    print(n)
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

def fuzzies(n):
    return fib(0, 1, n)

def fib(n, k, max):
    print(n)
    next = n + k
    if next < max:
        return fib(k, next, max)
    else:
        return next

factorial(10)
fuzzies(150)
