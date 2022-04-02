class Objeto():
    __atributoPrivado = None
    
    def __init__(self):
        self.__atributoPrivado = 0
        self.atributoPublico = "me lo ha pedido Jorge"
        
    def getAtributoPrivado(self):
        return self.__atributoPrivado
    
    def setAtributoPrivado(self, valor):
        self.__atributoPrivado = valor
        
    def atributoPrivado(self, valor=None):
        if valor == None:
            return self.__atributoPrivado
        else:
            self.__atributoPrivado = valor