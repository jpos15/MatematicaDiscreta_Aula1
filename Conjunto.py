class Conjunto():

    def __init__(self):
        self.elementos = []
        self.nome = None
        self.tamanho = 0

    def __str__(self):
        return str(self.elementos)

    def nomeConjunto(self, nome):
        self.nome = nome

    def limparString(self, valor):
        stringValor = valor.replace(" ", "")
        listaValor = stringValor.split(",")
        return listaValor

    def adicionar(self, valor):
        # listaValor = self.limparString(valor)
        for i in valor:
            if i not in self.elementos:
                self.elementos.append(i)
                self.tamanho += 1

    def adicionarSubConjunto(self, valor):
        listaValor = self.limparString(valor)
        c = Conjunto()
        for i in listaValor:
            if i not in c.elementos:
                c.adicionar(i)
                c.tamanho += 1
        self.adicionar([c.elementos])

    def imprimir(self):
        result = ""
        elemento = str(self.elementos)
        elemento = elemento.replace("[", "{")
        elemento = elemento.replace("]", "}")
        elemento = elemento.replace("'", "")
        print(self.nome, "=", elemento)
        print(self.elementos)
    
    def tamanhoConjunto(self):
        print("|" + self.nome + "|" , "=", self.tamanho)

    def pertence(self, valor):
        if valor in self.elementos:
            print("Pertence")
        else:
            print("Não pertence")

    def contem(self, valor):
        if valor in self.elementos:
            print("Contem")
            return True
        else:
            print("Não contem")
            return False

    def contemPropriamente(self, valor):
        if (self.contem(valor)):
            self.elementos.remove(valor)
            if len(self.elementos) >= 1:
                print("O Conjunto está contido propriamente ")                