class Conta:
    def __init__(self,numero, saldo = 0.0): #inicializador
        self.__numero = numero
        self.__saldo = saldo
    
    @property                               #decorator para acessar os parâmetros privados
    def numero(self):
        return self.__numero
    
    @property                               #decorator para acessar os parâmetros privados
    def saldo(self):
        return self.__saldo
    
    def depositar(self,valor):              #função/método para deposito
        self.valor = valor
        self.__saldo += self.valor
    
    def sacar(self,valor):                  #função/método para saque
        self.valor = valor
        self.__saldo -= self.valor
    
    pass

class ContaCorrente(Conta):
    def __init__(self,numero,taxa):              #inicializador
        Conta.__init__(self,numero)              #inicialização de classe derivada
        self.__taxa = taxa
    
    def cobrar_taxa(self):                        #função/método para retirar alguma taxa no saldo
        self.sacar(self.__taxa)                   #não usar a variável privada, mas as funções da Superclasse
    
    pass

class ContaPoupanca(Conta):
    def __init__(self,numero,juros):              #inicializador
        Conta.__init__(self,numero)               #inicialização de classe derivada
        self.__juros = juros
    
    def aplicar_juros(self):                      #função/método para aplicar juros no saldo
        self.depositar(self.saldo * self.__juros) #não usar a variável privada, mas as funções da Superclasse
                                                  #ainda que há parâmetros privados (não usar o doubleunderscore).
    
    pass
