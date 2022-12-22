from Simbolo import Simbolo
from TablaSimboloBase import TablaSimboloBase
from Automata import Automata

class Lexico:

    simbolos = []
    logSalida = ""

    def analizarLexema(self, lexema, tablaActual : TablaSimboloBase):
        simbolo = tablaActual.getSimboloByLexema(lexema)
        if simbolo == 0:
            if Automata.isIdentificador(lexema):
                simbolo = Simbolo("id", lexema, False)
            elif Automata.isNumero(lexema):
                simbolo = Simbolo("n_int", lexema, False)
            elif Automata.isReal(lexema):
                simbolo = Simbolo("n_float", lexema, False)
            
            if not tablaActual.existLexemaId(lexema):
                tablaActual.simbolosInicial.append(lexema)
        
        if simbolo != 0:
            self.logSalida = self.logSalida + "\tToken: " + simbolo.token + " Lexema: " + simbolo.lexema + "\n"
            self.simbolos.append(simbolo)
        else:
            self.logSalida = "\tERROR " + lexema + "\n"



    def analizarLinea(self, linea, tablaActual : TablaSimboloBase):
        self.simbolos.clear()
        self.logSalida = ""
        caracteres = list(linea)
        lexema = ""
        flagChar = False

        for car in caracteres:
            caracter = car + ""
            if flagChar:
                if caracter == '\\' :
                    flagChar = False
                    simbolo = Simbolo("string", lexema, False)
                    self.logSalida = self.logSalida + "\tToken: " + simbolo.token + " Lexema: " + simbolo.lexema + "\n"
                    self.simbolos.append(simbolo)
                    self.analizarLexema(caracter, tablaActual)
                    lexema = ""
                    continue
                lexema += caracter
                continue

            if tablaActual.isLexemaSimbolo(caracter):
                if caracter == '\\':
                    flagChar = True
                if lexema != "":
                    self.analizarLexema(lexema, tablaActual)
                lexema = ""
            elif caracter == " ":
                if lexema != "":
                    self.analizarLexema(lexema, tablaActual)
                lexema = ""
            
            else:
                lexema += caracter
        
        if lexema != "":
            self.analizarLexema(lexema, tablaActual)