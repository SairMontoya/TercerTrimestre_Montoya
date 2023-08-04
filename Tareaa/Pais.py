class Pais:
    def __init__(self,pais,pobla,altura,perpob):
        self.__pais=pais
        self.__pobla=pobla
        self.__altura=altura
        self.__perpob=perpob

    def info(self):
        return f"{self.__pais} {self.__pobla} {self.__altura} {self.__perpob}"
    
    def getPais(self):
        return self.__pais
    
    def getpobla(self):
        return self.__pobla
    
    def getaltura(self):
        return self.__altura
    
    def getPerpob(self):
        return self.__perpob