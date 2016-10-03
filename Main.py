import random
import time
import sys
from math import *
from squaresolver import *
from population import *

if __name__ == '__main__':
    start = time.clock()
    if(sys.argv[1]=='-help'):
        print("Resolverdor de cuadros magicos de n dimension \n 1er argumento: Dimensiones \n 2do argumento # de poblacion \n 3er argumento numero de muestra")
        sys.exit(0)
    n = sys.argv[1]
    pn = sys.argv[2]
    p= int(sys.argv[3])
    while True:
        c=0
        rep = 0
        scorec = 0
        ##g = input()
        #Pasar los datos de dim y pob por el metodo de create_population, devuelve una lista con los index del cubo y su dimensiones
        ind,b,bits_a,bitsn=create_population(int(n),int(pn))
        flag = False
        try:
            while True:
        #Convertimos cada uno de esos indices a un cubo magico con i2ms, devuelve un array de cubos magicos
                squares = i2ms(ind,b)
                scores,perfect = score(squares,start)
                ind = breed(bits_a,scores,p,bitsn,int(n))
                print("\r",max(scores))

                bits_a = to_bin(ind)
                c+=1
                if(rep == max(scores)):
                    scorec += 1
                rep = max(scores)
                if(scorec>20):
                    print("\n Proceso estancado, reintentando...")
                    print("---------------------------------------")
                    break
            #    time.sleep(1)
        except KeyboardInterrupt:
            print("proceso abortado")
            print("---------------------------------------")
            sys.exit()
        except ValueError:
            print("estancado en gen  ",c," reintentando...")
            print("---------------------------------------")
            pass
