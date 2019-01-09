#-5 a 5
#cifra 4

lista_letras = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t','u','v', 'w','x','y','z']
type(lista_letras)

frase = input ("Digite a frase:")
for x in frase:

    print (lista_letras.index(x) + 4)


