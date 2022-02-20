from functools import reduce

def firstChars(L):
    return (list(map(lambda x: x[0],L)))

def sum(L): 
    return reduce(lambda acc,b: acc + b,L)

def avg(L): #media
    return (reduce(lambda acc,b: acc + b,L)/len(L))

def maxString(L): #O primeiro termo é um acumulador, enquanto o segundo se modifica na estrutura
    return reduce(lambda x,y: x if len(x) > len(y) else y, L)

def add2Dict(D, N, S): #modo mais simples: D[N] = D[N] + [S] if N in D else [S] / return D
    for key,value in D.items():
        if key == N: #se tiver a mesma key o dado é adicionado
            D[key] += [S]
            return D
    D[N] = [S] #caso contrario é feito uma nova key com um novo dado
    return D

def buildLenFreq(L):
    D = dict()
    for i in range(len(L)):
        add2Dict(D,len(L[i]),L[i])
    return D

def incValue(D,N): #modo mais simples: D[N] = D[N] + 1 if N in D else 1 / return D
    for key,value in D.items():                         #o "N in D" é o que ocasiona o loop
        if key == N: 
            D[key] += 1
            return D
    D[N] = 1
    return D

def countFirsts(L):
    D = dict()
    for i in firstChars(L):
        D = incValue(D,i)
    return D

def mostCommonFirstCharFreeLoop(L): #free loop # cria-se duas listas em que a primeira contem keys e a segunda os valores
    return (list(countFirsts(L).keys())   [list(countFirsts(L).values()).index(reduce(lambda acc, value: acc if acc > value else value, countFirsts(L).values()))])
    
def mostCommonFirstChar(L):
    a = 0
    D = countFirsts(L)
    for key,value in D.items():
        if a < value:
            a = value
            b = key
    return b

