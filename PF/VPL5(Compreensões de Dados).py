from functools import reduce

def delInitials(L):
   return ', '.join([string.capitalize() for string in L if len(string) > 1])

def everyOccurrence(S,Q):
    L = [num for letterQ in Q for num,letterS in enumerate(S) if letterS == letterQ]
    L.sort()
    return L

def factors(N):
    return [num for num in range(N) if num != 0 and num != 1 if N%num == 0]

import operator
def isPerfect(N):
    return True if (reduce(operator.add,factors(N)) + 1) == N else False


