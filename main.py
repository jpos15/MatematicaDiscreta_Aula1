import Conjunto
c = Conjunto.Conjunto()

# Nome do conjunto
c.nomeConjunto("A")

# Adicionando itens ao conjunto
c.adicionar("abc")

# Adicionando dois subconjuntos
c.adicionarSubConjunto("1,2,3")

# Imprimindo o conjunto completo
c.imprimir()

# Imprimindo o tamanho do conjunto
c.tamanhoConjunto()

c.pertence("a")
c.pertence("b")
c.pertence("b")
c.pertence("d")
c.pertence(["1","2","3"])

c.contem(["1","2","4"])
c.contem(["1","2","3"])

c.contemPropriamente(["1","2","3"])





