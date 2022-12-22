import json
import os

class Simbolo:
    
    token = ""
    lexema = ""
    palabraReservada = False

    def __init__(self, token, lexema, palabraReservada):
        self.token = token
        self.lexema = lexema
        self.palabraReservada = palabraReservada

    def __iter__(self):
        yield from {
            "token": self.label,
            "lexema": self.x,
            "palabraReservada": self.y
        }.items()

    @staticmethod
    def from_json(json_dct):
        return Simbolo(json_dct['token'],
                   json_dct['lexema'], json_dct['palabraReservada'])

    @staticmethod
    def crearLista():
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        
        __location__ = os.path.join(__location__, "Tabla de Simbolos.json")

        tabla = open(__location__)

        tabla = json.load(tabla)

        lista = []

        for i in tabla:
            lista.append(Simbolo.from_json(i))
        
        return lista