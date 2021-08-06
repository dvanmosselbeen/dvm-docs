#!/usr/bin/env python3

def decorate(function):
    def handler():
        return function().upper()
    return handler

def decorateOther(function):
    def handler():
        return function().lower()
    return handler


@decorate
def returnMsg():
    return "Hello World"

@decorateOther
def returnMsg2():
    return "HELLO PLANET!"

@decorate
def returnMsg3():
    return "Hello World"


print(returnMsg())
print(returnMsg2())
print(returnMsg3())
