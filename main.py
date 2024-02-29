import matplotlib.pyplot as plt
import numpy as np
import math
        
def ex ():

    x = np.linspace(0, 0.1, 5)
    y = (-5) * np.cos(10*x) * ((np.sin(3*x))/(x*x))

    plt.plot(x, y)
    plt.savefig('Ex1.png')
    plt.show()

def ex1 ():
    s="Atrgfjxvythvllxxxcccxhhqzbygibb"
    dictionary = {}
    for i in s:
        dictionary[i] = s.count(i)
    print(dictionary)
    plt.bar(dictionary.keys(), dictionary.values(), width=0.5, color='g')

    plt.xlabel('Char')
    plt.ylabel('Numb')
    plt.title('Ex.2')
    plt.savefig('Ex2.png')
    plt.show()

def ex2 ():

    s="ajvn! Dthgyvk... Lpcyxhs? SvrdV? fvdv? vvds! kfov. Lpo..."
    s1=s.split(" ")
    s2=[]
    
    for i in s1:
        for j in i:
            if(j=='!'or j=='?' or j=='.'):
                s2.append(j)
    
    #print(s2)

    dictionary = {}
    for i in s2:
        dictionary[i] = s2.count(i)
    #print("D: ")
    #print(dictionary)
    dictionary['...']=s.count('...')
    #print("S: ",s.count('...'))
    dictionary['.']=(int(dictionary['.'])-3*s.count('...'))
    print("D1: ")
    print(dictionary)
    
    plt.bar(dictionary.keys(), dictionary.values(), width=0.5, color='b')

    plt.xlabel('Symb')
    plt.ylabel('Numb')
    plt.title('Ex.3')
    plt.savefig('Ex3.png')
    plt.show()


print ("N: ")
n = int(input())

match n:
        case 1:
            ex()
        case 2:
            ex1()
        case 3:
            ex2()
        case default:
            print ("Error")