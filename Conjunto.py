
class Conjunto():

    def __init__(self):
        self.elementos = []
        self.nome = None
        self.tamanho = 0

    def nomeConjunto(self, nome):
        self.nome = nome

    def adicionar(self, valor):
        if valor in self.elementos:
            print("Deu ruim")
        else:
            self.elementos.append(valor)
            self.tamanho += 1
            print("Valor inserido com sucesso")
            # print(self.elementos)

    def imprimir(self):
        result = ""
        for i in self.elementos:
            result += str(i) + ","
        print( self.nome, "= " "{",result,"}")
        # print(self.nome, self.elementos)
        # print("Tamanho do conjunto:", self.tamanho)