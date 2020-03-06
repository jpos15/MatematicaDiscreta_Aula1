from Conjunto import *

a = Conjunto()

# Nome do conjunto
a.nomeConjunto('A')

# Adicionando itens ao conjunto
a.adicionar('a, b, c')
a.adicionar('1,2,3,5,6,7')

# b = Conjunto()
# b.nomeConjunto('B')
# b.adicionar('2,3,5,9')

# d = Conjunto()
# d.nomeConjunto('Conjunto união')
# d.uniao(a, b)
# d.imprimir()

# Adicionando subconjuntos
z = Conjunto()
z.nomeConjunto('z')
z.adicionar("1, 2, 3")
z.imprimir()

a.adicionarSubConjunto(z.elementos)

a.imprimir()

# Imprimindo o conjunto completo
# a.imprimir()
# b.imprimir()

# Imprimindo o tamanho do conjunto
# c.tamanhoConjunto()

# Verificando se os elementos pertencem ao conjunto
# c.pertence("a")
# c.pertence("z")
# c.pertence("b")
# c.pertence("d")

# Verificando se o conjunto passado por parametros pertence ao conjunto criado
# c.pertence({1,2,3})

# Verificando se o conjunto passado por parametros contem no conjunto criado
# c.contem({1,2,3})

# No momento tem que passar como lista, mas será alterado
# c.contemPropriamente({1,2,3})


##########################################################################################################
