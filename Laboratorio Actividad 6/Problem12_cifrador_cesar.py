# cifrador_cesar.py
class CifradorCesar:
    def __init__(self, desplazamiento):
        self.desplazamiento = desplazamiento
        self.SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' +      
                  'abcdefghijklmnopqrstuvwxyz1234567890 !?.'
    def cifrar(self, mensaje):
        mensajec = ""
        longitud = len(self.SYMBOLS)
        for letra in mensaje:
            if letra not in self.SYMBOLS:
                mensajec += letra
                continue
            i = self.SYMBOLS.index(letra) + self.desplazamiento
            if i >= longitud:
                i -= longitud
            mensajec += self.SYMBOLS[i]
        return mensajec

    def descifrar(self, mensajec):
        mensajed = ""
        for letra in mensajec:
            if letra not in self.SYMBOLS:
                mensajec += letra
                continue
            i = self.SYMBOLS.index(letra) - self.desplazamiento
            mensajed += self.SYMBOLS[i]
        return mensajed
