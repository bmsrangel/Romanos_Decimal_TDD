class NumerosRomanos:
    def __init__(self):
        self.romanos = {'M': 1000, 'CM': 900, 'D': 500, 'C': 100, 'XC': 90, 'L': 50, 'X': 10, 'IX': 9, 'V': 5, 'I': 1}

    def dec2rom(self, numero):
        numero = int(numero)
        anterior = None
        aux = dict()
        lista_aux = list()
        aux['M'] = numero // 1000
        numero %= 1000
        aux['CM'] = numero // 900
        numero %= 900
        aux['D'] = numero // 500
        numero %= 500
        aux['C'] = numero // 100
        numero %= 100
        aux['XC'] = numero // 90
        numero %= 90
        aux['L'] = numero // 50
        numero %= 50
        aux['X'] = numero // 10
        numero %= 10
        aux['IX'] = numero // 9
        numero %= 9
        aux['V'] = numero // 5
        numero %= 5
        aux['I'] = numero
        for k, v in aux.items():
            if k != 'M' and v == 4:
                lista_aux.append(k)
                for k2, v2 in aux.items():
                    if k2 != k:
                        anterior = k2
                    else:
                        break
                lista_aux.append(anterior)
            else:
                for c in range(v):
                    lista_aux.append(k)
        saida = ''.join(i for i in lista_aux)
        return saida

    def rom2dec(self, numero):
        saida = 0
        numero = list(str(numero).upper())
        for c in range(len(numero)):
            if c < len(numero)-1:
                if self.romanos[numero[c]] < self.romanos[numero[c+1]]:
                    saida -= self.romanos[numero[c]]
                else:
                    saida += self.romanos[numero[c]]
            else:
                saida += self.romanos[numero[c]]
        return abs(saida)
