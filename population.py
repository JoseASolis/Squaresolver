import random
import time
import sys
from math import *


def create_population(dim,pn):
    t = log(factorial(dim**2),2)
    fac = factorial(dim**2)
    b = int(t+1)
    d = ""
    divisor = fac +int(fac*.10)
    indarray = []
    bits_array=[]
    #print("bits usados: ",b)
    for x in range(pn):
        for y in range(b) :
            if random.randint(0,divisor) %2:
                d = "1"+d
            else:
                d="0"+d

            num=int(d,2)%factorial(dim**2)
        bits_array.append(d)
        indarray.append(num)

        #print("\n index #",len(indarray),": ",num)
        d=""
    return indarray,dim,bits_array,b
