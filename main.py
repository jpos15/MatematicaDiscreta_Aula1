import Conjunto
c = Conjunto.Conjunto()

# Nome do conjunto
c.nomeConjunto("ConjuntoTeste")

# Adicionando itens ao conjunto
c.adicionar("2")
c.adicionar(3)

c.adicionar("A")
c.adicionar(4)
c.adicionar(3)

# Adicionando dois subconjuntos
c.adicionarSubConjunto("5, 10, 25,   5, 45")
c.adicionarSubConjunto(9)

# Adicionando mais itens ao conjunto principal
c.adicionar(6)
c.adicionar(8)
c.adicionar(9)
c.adicionar(1)

# Imprimindo o conjunto completo
c.imprimir()

# Imprimindo o tamanho do conjunto
c.tamanhoConjunto()


