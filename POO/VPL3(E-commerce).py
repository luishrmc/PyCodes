from abc import *
class Item(ABC):
    def __init__(self,nome,valor):
        self.__nome = nome
        self.__valor = valor
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def valor_semdesc(self):
        return self.__valor
    
    def valor_desc(self):
        return self.valor_semdesc*self.desc_item()
    
    @abstractmethod
    def desc_item(self): #operações específicas de cada objeto
        pass

    @abstractmethod
    def tipo_item(self):
        pass
    pass
   

class Livro(Item):
    def __init__(self,nome,valor):
        super().__init__(nome,valor) #atributos nome e valor são herdados da classe abstrata
        self.desc = 0.97             #atributos individuais de cada objeto
        self.tipo = "Livro"
    
    def desc_item(self):             #cumprimento do contrato
        return self.desc
    
    def tipo_item(self):
        return self.tipo
    pass
    
    
class Brinquedo(Item):
    def __init__(self,nome,valor):
        super().__init__(nome,valor) #atributos nome e valor são herdados da classe abstrata
        self.desc = 0.95             #atributos individuais de cada objeto
        self.tipo = "Brinquedo"
    
    def desc_item(self):             #cumprimento do contrato
        return self.desc
    
    def tipo_item(self):
        return self.tipo
    pass


class Eletronico(Item):
    def __init__(self,nome,valor):
        super().__init__(nome,valor) #atributos nome e valor são herdados da classe abstrata
        self.desc = 0.92             #atributos individuais de cada objeto
        self.tipo = "Eletronico"
    
    def desc_item(self):             #cumprimento do contrato
        return self.desc
    
    def tipo_item(self):             #é possível usar também obj.tipo definido no inicializador
        return self.tipo
    pass


class CestaCompras:
    def __init__(self):
        self.itens = {}
    
    def adicionar_item(self,item,qtde):
        self.itens[item] = qtde
    
    def relatorio_final(self):
        sum = 0                              #somar os valores com o desconto de cada obj
        for key,value in self.itens.items():
            sum += key.valor_desc()*value
        print("%.2f" %sum)

        for key,value in self.itens.items():
            print("%s, %s, %i, %.2f, %.2f, %.2f" %(key.tipo_item(), key.nome, value, key.valor_semdesc, key.valor_semdesc*value, key.valor_desc()*value ), end='\n')
    pass