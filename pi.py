#Calculates pi using the Gregory-Leibniz series.

from math import *
from random import *

iterations = 10000

divisor=1.0
switch=False
pie=4/divisor

for x in range(0,iterations):
  divisor+=2
  if switch:
    pie+=4/divisor
    switch=False
  else:
    pie-=4/divisor
    switch=True
    print (pie)
print
print (pi)
print
