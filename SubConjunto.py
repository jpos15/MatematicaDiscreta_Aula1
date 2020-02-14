class SubConjunto():

    def __init__(self):
        self.elementos = []
        self.tamanho = 0

    def adicionarSubConjunto(self, valor):
        if valor in self.elementos:
            return False
        else:
            self.elementos.append(valor)
            self.tamanho += 1
            return self.elementos

    def tamanhoSubConjunto(self):
        return self.tamanho