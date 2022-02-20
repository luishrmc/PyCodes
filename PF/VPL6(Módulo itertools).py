from itertools import *
dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
periodos = ["D","N"]

def buildTurns(profs):
    turns = product(dias,periodos)
    tXprof = zip(turns, cycle(profs), count(1))
    return [(d_semana, peri, nome, indice) for (d_semana,peri), nome, indice in tXprof]

def printCSV(profs):
    print("indice, dia, periodo, profissional")
    trab = buildTurns(profs)
    for (d_semana,peri,nome,indice) in trab:
        print("%s, %s, %s, %s" %(indice, d_semana, peri, nome))
    return 'fim'

def firstDay(profs, prof):
    trab = buildTurns(profs)
    for (d_semana,peri,nome,indice) in trab:
        if prof == nome:
            return d_semana
    return "Inexistente"

def countTurns(profs, prof):
    trab = buildTurns(profs)
    return print(len(list(filter(lambda x: x[2] == prof,trab))))

def payTurns(profs,prof):
    trab = buildTurns(profs)
    sal = 0
    for (d_semana,peri,nome,indice) in trab:
        if prof == nome:
            if peri == 'D':
                sal += 1000
            else:
                sal += 1333
    return sal
    