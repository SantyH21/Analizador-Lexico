from Simbolo import Simbolo

class TablaSimboloBase :

    def __init__(self):
        self.simbolosInicial = Simbolo.crearLista()
    
    def getSimboloByLexema(self, lexema):
        
        for simbolo in self.simbolosInicial:
            if simbolo.lexema == lexema:
                return simbolo
        
        return 0
    
    def isLexemaSimbolo(self, lexema):
        for simbolo in self.simbolosInicial:
            if simbolo.lexema == lexema and simbolo.palabraReservada:
                return True
        
        return False

    def existLexemaId(self, lexema):
        for simbolo in self.simbolosInicial:
            if simbolo.lexema == lexema and simbolo.palabraReservada == False:
                return True
        
        return False