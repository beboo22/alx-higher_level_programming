#!/usr/bin/python3

def find_peak(list_of_integers):
   x = len(list_of_integers)
   if (x == 0):
    return None
   if (list_of_integers[0] > list_of_integers[1]):
    return list_of_integers[0]

   if (list_of_integers[x] > list_of_integers[x-1]):
    return list_of_integers[x]

   for i in range(x):

