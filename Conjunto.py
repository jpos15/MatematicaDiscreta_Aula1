bd = {}

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

    def adicionar(self, *valor):
        if valor is None:
            print('Vazio')
            return False
        else:
            # listaValor = self.limparString(valor)
            for i in valor:
                if i not in self.elementos:
                    self.elementos.append(i)
                    self.tamanho += 1

    def adicionarSubConjunto(self, valor):
        self.elementos.append(valor)
        self.tamanho += 1

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
        return elemento
    
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
            print("O conjunto:", elemento, "não está contifo no conjunto:", listaElementos)
            return False

    def contemPropriamente(self, valor):
        if (self.contem(valor)):
            listaElementos = self.limpar(str(self.elementos))

            elemento = str(valor)
            elemento = self.limpar(elemento)
            listaElementos.replace(elemento, '')
            if len(self.elementos) >= 1:
                print("E o Conjunto", elemento, "também está contido propriamente no conjunto:", listaElementos)

    def uniao(self, conjunto1, conjunto2):
        if len(conjunto1.elementos) == 0:
            self.elementos = conjunto2.elementos
            print('Conjunto 1 é vazio')

        elif len(conjunto2.elementos) == 0:
            self.elementos = conjunto1.elementos
            print('Conjunto 2 é vazio')

        elif len(conjunto1.elementos) != 0 and len(conjunto2.elementos) != 0:
            print('São vazios')

        elif conjunto1.elementos == conjunto2.elementos:
            self.elementos = conjunto1.elementos
            print('É igual')
        
        else:
            print('É diferente')
            self.elementos = conjunto1.elementos
            for i in conjunto2.elementos:
                self.adicionar(i)

        bd[conjunto1.nome + conjunto2.nome]=self.elementos
        print('Dicionario', bd)

        # print(conjunto1.elementos, conjunto2.elementos)
