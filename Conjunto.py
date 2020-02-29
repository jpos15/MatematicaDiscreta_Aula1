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
        listaValor = self.limparString(valor)
        for i in listaValor:
            if i not in self.elementos:
                self.elementos.append(i)
                self.tamanho += 1

    def adicionarSubConjunto(self, valor):
        self.elementos.append(valor)
        self.tamanho += 1

    def SubConjunto(self, valor):
        listaValor = self.limparString(valor)
        c = Conjunto()
        for i in listaValor:
            if i not in c.elementos:
                c.adicionar(i)
                c.tamanho += 1
        self.adicionarSubConjunto(c.elementos)

    def limpar(self, listaStr):
        elemento = listaStr
        # print(elemento)
        elemento = elemento.replace("[", "{")
        elemento = elemento.replace("]", "}")
        elemento = elemento.replace("'", "")
        return elemento

    def imprimir(self):
        elemento = str(self.elementos)
        elemento = self.limpar(elemento)
        print(self.nome, "=", elemento)
    
    def tamanhoConjunto(self):
        print("|" + self.nome + "|" , "=", self.tamanho)

    def pertence(self, valor):
        listaElementos = self.limpar(str(self.elementos))

        elemento = str(valor)
        elemento = self.limpar(elemento)
        if elemento in listaElementos:
            print(elemento, "pertence ao conjunto:", listaElementos)
        else:
            print(elemento, "não pertence ao conjunto", listaElementos)

    def contem(self, valor):
        listaElementos = self.limpar(str(self.elementos))

        elemento = str(valor)
        elemento = self.limpar(elemento)
        if elemento in listaElementos:
            print("O conjunto:", elemento, "está contido no conjunto:", listaElementos)
            return True
        else:
            print("O conjunto:", elemento, "não está contido no conjunto:", listaElementos)
            return False

    def removeElementos(self):
        self.elementos = []
        self.tamanho = 0

    def contemPropriamente(self, valor):
        if (self.contem(valor)):
            listaElementos = self.limpar(str(self.elementos))

            elemento = str(valor)
            elemento = self.limpar(elemento)
            listaElementos.replace(elemento, '')
            if len(self.elementos) >= 1:
                print("E o Conjunto", elemento, "também está contido propriamente no conjunto:", listaElementos)

    def uniaoConjuntos(self, conj1, conj2):
        segura=[]
        if conj1.contem(conj2):
            self.adicionar(conj1.elementos)
            self.tamanho = conj1.tamanho
            self.nome = str(conj1.nome, ' ∩ ', conj2.nome)
            print(self.nome, '=', self.__str__())
        else:
            for i in conj1.elementos:
                for a in conj2.elementos:
                    if i == a:
                        return False
                    else:
                        self.adicionar(a)
                if 