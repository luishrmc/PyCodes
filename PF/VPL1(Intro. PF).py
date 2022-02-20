def head(L):     #Conseguir o primeiro termo
    return L[0]

def tail(L):     #Conseguir a calda
    return L[1]

def py2ll(L):    #Transmutar de Lista para Lista Encadeada
    if not L: 
        return None
    else:
        return (L[0], py2ll(L[1:]))
    
def ll2py(L):    #Transmutar de Lista Encadeada para Lista
    if not L:
        return []
    else:
        H = head(L)
        T = tail(L)
        return [H] + ll2py(T)

def size(L):    #Saber o tamanho do Lista encadeada
    if not L:
        return 0
    else:
        return 1 + size(tail(L))

def sorted(L):  #Saber se a Lista Encadeada está ordenada
    if not L:
        return True
    elif not tail(L):
        return True
    else:
        C1 = head(L) <= head(tail(L))
        return C1 and sorted(tail(L))
 
def sum(L):       #Soma dos elementos da Lista Encadeada
    if not tail(L):
        return head(L)
    else:
        return head(L) + sum(tail(L))

def split(L):   #Dividir a Lista Encadeada em outras Listas Encadeadas
    if not L:
        return (None,None)
    if not tail(L):
        return(L,None)
    else:
        H0 = head(L)
        H1 = head(tail(L))
        (T0, T1) = split(tail(tail(L)))
        return ((H0, T0), (H1, T1))

def merge(L0,L1):    #Ordenar os termos da Lista Encadeada
    if not L0:
        return L1
    if not L1:
        return L0
    else:
        H0 = head(L0)
        T0 = tail(L0)
        H1 = head(L1)
        T1 = tail(L1)
        if H0 < H1:
            return (H0, merge(T0, L1))
        else:
            return (H1, merge(L0, T1))

def mSort(L): #Ordenador final de Listas Encadeadas
    if not L:
        return None
    if not tail(L):
        return L
    else:
        (L0, L1) = split(L)
        return merge(mSort(L0), mSort(L1))

def max(L): #Valor máximo da função !!!
    if not tail(L):
        return head(L)
    else:
        m = max(tail(L))
        return m if m > head(L) else head(L)

def get(L,N): #O mesmo pensamento recursivo de max, mas sem a operação no final
    if N == 0:
        return head(L)
    v = get(tail(L),N-1)
    return v
