import random
import time
import sys
from math import *

def init_a(b):
    a=[]
    for i in range(b**2):
        a.append(i+1)
    return a
def i2ms(index,b):
    squares=[]
    a= init_a(b)
    i=0
    t=b
    b = (b**2)-1
    for i in range(len(index)):

        s=""
        cont = 1
        while(index[i]>0):
            c = factorial(b)
            ind =(index[i]/c)
            s = s+str(a[int(ind)])+" "
            del a[(int(ind))]
            index[i] = index[i]%c
            b-=1
            cont +=1
        for i in range(len(a)):
            s = s+str(a[i])+" "
        squares.append(s)
        a = init_a(t)
        b = t
        b = (b**2)-1
        s=""
    return squares
    del squares,a,i,t,b,cont,c,s
def score(squares,start):
    scores=[]
    print("\n")
    for i in range(len(squares)):
        r = squares[i]
        r = r.split(' ')
        n = int(sqrt(len(r)))
        nd = r
        goal = n * (n * n + 1) / 2;
        nd.reverse()
        m = [[nd.pop() for i in range(n)] for j in range(n)]
        min_sum,max_sum= 0,0
        minn = 1
        maxx = n * n
        for i in range (n):
            min_sum += minn
            minn += 1
            max_sum += maxx
            maxx += 1
        min_b,max_b = abs(goal - min_sum), abs(goal - max_sum)
        if min_sum < max_sum:
             final_b = max_sum
        else:
            final_b = min_sum
        total_cases = 2 * n + 2
        bias = total_cases * final_b
        fitness = bias
        for i in range(n):
            s =0
            for j in range(n):
                s +=int(m[i][j])
            fitness -= abs(goal-s)
        for j in range(n):
            s=0
            for i in range(n):
                s += int(m[i][j])
            fitness -= abs(goal-s)
        s = 0

        if n%2 == 1:
            for i in range(n):
                s+= int(m[i][i])
            fitness -= abs(goal-s)
            m.reverse()
            s = 0
            for i in range(n):
                s+= int(m[i][i])
            fitness -= abs(goal-s)
        if(fitness==bias):
            print("perfect score ", bias)
            print("Cubo encontrado en ",round(time.clock()-start,2), " segundos \n")
            for row in m:
                print (row)
            sys.exit()
        scores.append(int(fitness))
    return scores,bias
def to_bin(d):
    binarray = []
    for i in d:
        binarray.append(bin(i))
    return binarray
def breed(popul,score,breed_size,b,n):
    pobl = popul
    pop_num_target = len(popul) - breed_size
    maxx = max(score)
    breed_pop=[]
    new_pop=[]
    tempscore = score
    for y in range(breed_size):
        for z in range(len(score)):
            if z<len(score):
                if score[z] == maxx:
                    breed_pop.append(pobl[z])
                    del score[z]
                    del pobl[z]
                    maxx= max(score)
    del pobl
    while(len(breed_pop)>breed_size):
        breed_pop.pop()
    while len(new_pop)<pop_num_target:
        rand1 = random.randint(0,len(breed_pop)-1)
        rand2 = random.randint(0,len(breed_pop)-1)
        mutate= random.randint(1,100)
        mutate_chance = 100
        while(rand2==rand1):
            rand2= random.randint(0,len(breed_pop)-1)
        if((b%2)==0):
            halfp=int((b)/2)
            newind = breed_pop[rand1][:halfp]+""+ breed_pop[rand2][halfp:]
            if mutate > mutate_chance:
                randomp = random.randint(0,len(newind))
                if newind[randomp] == '0':
                    newind[randomp] = '1'
                else:
                    newind[randomp] = '0'
            new_pop.append((newind))
        else:
            halfo=int((b-1)/2)
            newind = breed_pop[rand1][:halfo] + breed_pop[rand2][halfo:]
            if mutate > mutate_chance:
                randomp = random.randint(0,len(newind))
                if newind[randomp] == '0':
                    newind[randomp] = '1'
                else:
                    newind[randomp] = '0'
            new_pop.append(newind)
    for i in breed_pop:
        new_pop.append(i)
    for i in range(len(new_pop)):
        new_pop[i] = int(new_pop[i],2)
        new_pop[i]= new_pop[i]%(factorial(n**2))
    del newind,rand1,rand2,pop_num_target,maxx,breed_pop,tempscore,score,popul,breed_size
    return new_pop
