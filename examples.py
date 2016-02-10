# -*- coding: utf-8 -*-
__author__ = "karnikamit"


# get even numbers
nos = range(100)
print filter(lambda x: x % 2 == 0, nos)

# get odd numbers
print filter(lambda x: x % 2, nos)