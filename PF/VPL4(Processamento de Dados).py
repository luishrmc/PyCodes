def lastNames(L):
    return list(map(lambda x: x[len(x)-1],L)) 

def citations(L):
    return list(map(lambda x: x[0][0].capitalize() + '. ' + x[len(x)-1],L))

#por recursividade 
def fullCitations(L):
    def fcit(lis):
        if len(lis) == 1:
            return lis[0]
        return lis[0][0].capitalize() + '. ' + fcit(lis[1:])
    return list(map(lambda x: fcit(x),L))

#por iteração
def fullCitations(L):
    def fcit(lis):
        first_letters = str()
        for i in range(len(lis)-1):
            first_letters += (lis[i][0].upper() + '. ')
        return first_letters + lis[len(lis)-1].capitalize()
    return list(map(lambda x: fcit(x),L))

