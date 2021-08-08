#!/usr/bin/env python3

"""
A little example of if <something> in a-string.
"""

a = "thm{you-got-the-flag}"

if "thm" in a:
    print("You got the flag!" + a)
else:
    print("nope")
