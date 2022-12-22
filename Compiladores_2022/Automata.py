import string

from Simbolo import Simbolo


class Automata:

    @staticmethod
    def isIdentificador(lexema):
        letras = list(string.ascii_letters)
        digitoletra = list("0123456789" + string.ascii_letters)
        caracter = ''
        estado = 1
        reservadas = []
        lista = Simbolo.crearLista()
        lexema = str(lexema)

        for simbolo in lista:
            reservadas.append(simbolo.lexema)
            
        if lexema in reservadas:
            return False

        for i in lexema:
            caracter = i + ""
            match estado:
                case 1:
                    if caracter in letras:
                        estado = 2
                    else:
                        estado = 3
                    break
                
                case 2:
                    if caracter in digitoletra:
                        estado = 2
                    else:
                        estado = 3
                    break

        if estado != 3:
            return True

        return False
                
    @staticmethod
    def isNumero(lexema):
        digito = list("0123456789")
        caracter = ''
        estado = 1
        lexema = str(lexema)
        for i in lexema:
                caracter = i + ""
                match estado:
                    case 1:
                        if caracter in digito:
                            estado = 1
                        else:
                            estado = 2
                        
        
        if estado != 2:
            return True
        
        return False

    @staticmethod
    def isReal(lexema):
        caracter = ''
        estado = 1
        i = 0

        while i < len(lexema):
            caracter = lexema[i] + ""
            match estado:
                case 1:
                    if Automata.isNumero(caracter):
                        estado = 1
                        i = i+1 
                    else:
                        estado = 2
                    
                    
                case 2:
                    if caracter == '.':
                        if i+1 != len(lexema):
                            estado = 3
                        else:
                            estado = 4
                    else:
                        estado = 4
                        break
                    i = i+1 
                    

                case 3:
                    if Automata.isNumero(caracter):
                        estado = 3
                    else:
                        estado = 4
                        break
                    i = i+1 
                    
        
        if estado != 4:
            return True
        else:
            return False