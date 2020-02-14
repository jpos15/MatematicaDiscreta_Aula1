import SubConjunto

subContjunto = SubConjunto.SubConjunto()

class Conjunto():

    def __init__(self):
        self.elementos = []
        self.nome = None
        self.tamanho = 0

    def nomeConjunto(self, nome):
        self.nome = nome

    def adicionar(self, valor):
        if valor not in self.elementos:
            self.elementos.append(valor)
            self.tamanho += 1

    def adicionarSubConjunto(self, valor):
        x = subContjunto.adicionarSubConjunto(valor)
        if x:
            self.adicionar(x)
            print("Valor inserido com sucesso")

    def imprimir(self):
        result = ""
        elemento = str(self.elementos)
        elemento = elemento.replace("[", "{")
        elemento = elemento.replace("]", "}")
        elemento = elemento.replace("'", "")
        print(self.nome, "=", elemento)
    
    def tamanhoConjunto(self):
        print("Tamanho do conjunto:", self.tamanho)

    def tamanhoSubConjunto(self):
        print("Tamanho do subconjunto:", subContjunto.tamanhoSubConjunto())