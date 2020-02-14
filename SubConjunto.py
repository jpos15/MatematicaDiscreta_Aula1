class SubConjunto():

    def __init__(self):
        self.elementos = []
        self.nome = None
        self.tamanho = 0

    def nomeSubConjunto(self, nome):
        self.nome = nome

    def adicionarSubConjunto(self, valor):
        if valor in self.elementos:
            return False
        else:
            self.elementos.append(valor)
            self.tamanho += 1
            return self.elementos

    def tamanhoSubConjunto(self):
        return self.tamanho