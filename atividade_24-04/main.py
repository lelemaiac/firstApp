#Ciar uma lista com nome de 5 objetos
objetos = ["Garrafa", "Lápis", "Caderno", "Mouse", "Computador"]
print("Lista de objetos criada com sucesso: ", objetos)

#Adicionar mais um objeto ao final da lista
objetos.append("Óculos")
print("Objeto adicionado com sucesso: ", objetos)

#Acessar o objeto que está na 2º posição
acessar = objetos[2]
print("Objeto acessado com sucesso: ", acessar)

#Remover um objeto da lista
objetos.remove("Garrafa")
print("Objeto removido com sucesso: ", objetos)

#Exibir o tamanho da lista
len(objetos)
print("Número de objetos listado com sucesso: ", len(objetos))

#Mostrar todos os itens como um laço for
for objeto in objetos:
    print(objeto, "Lista percorrida com sucesso")

#Verificar se "Cadeira" está na lista, se sim remova, se não, adicione
if "Cadeira" in objetos:
    objetos.remove("Cadeira")
    print("Objeto removido com sucesso: ", objetos)
else:
    objetos.append("Cadeira")
    print("Objeto adicionado com sucesso: ", objetos)

#Ordenar a lista em ordem alfabéica
objetos.sort()
print("Objeto ordenado com sucesso: ", objetos)

#Exibir o primeiro e o último objeto
objeto_1 = objetos[0]
objeto_ultimo = objetos[len(objetos) -1]
print("Objetos exibidos com sucesso: ", objeto_1,"e", objeto_ultimo)

#Limpar toda a lista
objetos.clear()
print("Lista limpa com sucesso: ", objetos)
