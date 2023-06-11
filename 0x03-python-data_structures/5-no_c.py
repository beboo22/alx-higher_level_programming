#!/usr/bin/python3
def no_c(my_string):
    n_str = ""
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            n_str += letter
    return n_str
