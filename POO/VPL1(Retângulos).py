class Ponto2D:

    def __init__ (self, x = 0.0, y = 0.0): #inicializador
        self.x = x
        self.y = y
    pass

class Retangulo:

    def __init__ (self,esq_sup,dir_inf): #inicializador
        self.__esq_sup = esq_sup
        self.__dir_inf = dir_inf
    
    @property                           #decorator para os parâmetros privados
    def esq_sup(self):
        return self.__esq_sup
    
    @property                           #decorator para os parâmetros privados
    def dir_inf(self):
        return self.__dir_inf
    
    @property                           #decorator para usar os parãmetros privados
    def width(self):
        return  self.__dir_inf.x - self.__esq_sup.x
    
    @property                           #decorator para usar os parãmetros privados
    def height(self):
        return self.__esq_sup.y - self.__dir_inf.y
    
    def calcularArea(self):             #utilizar o self para que a função não seja estática
        return (self.__esq_sup.y - self.__dir_inf.y)*(self.__dir_inf.x - self.__esq_sup.x)
    
    def calcularIntersecao(self,ret):
        #sem intersecao
        if(ret.__dir_inf.y > self.__esq_sup.y or ret.__esq_sup.y < self.__dir_inf.y or ret.__dir_inf.x < self.__esq_sup.x or ret.__esq_sup.x > self.__dir_inf.x):
            return (None)
        #intersecao
        elif(ret.__esq_sup.y > self.__esq_sup.y):
            #caso especifico
            if(self.__esq_sup.x < ret.__esq_sup.x and ret.__esq_sup.x < self.__dir_inf.x):
                return (ret.__dir_inf.x - ret.__esq_sup.x)*(self.__esq_sup.y - ret.__dir_inf.y)
            #restante
            elif(self.__esq_sup.x < ret.__dir_inf.x and ret.__dir_inf.x < self.__dir_inf.x):
                return (self.__esq_sup.y - ret.__dir_inf.y)*(ret.__dir_inf.x - self.__esq_sup.x)
            elif(ret.__dir_inf.x > self.__dir_inf.x):
                return(self.__dir_inf.x - ret.__esq_sup.x)*(self.__esq_sup.y - ret.__dir_inf.y)
                
        elif(ret.__esq_sup.y < self.__esq_sup.y):
            if(self.__esq_sup.x < ret.__dir_inf.x and ret.__dir_inf.x < self.__dir_inf.x):
                return (ret.__esq_sup.y - self.__dir_inf.y)*(ret.__dir_inf.x - self.__esq_sup.x)
            elif(ret.__dir_inf.x > self.__dir_inf.x):
                return (self.__dir_inf.x - ret.__esq_sup.x)*(ret.__esq_sup.y - self.__dir_inf.y)
    pass