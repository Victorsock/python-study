# Listas em Python
#print("### Listas ###")
# Listas são estruturas de dados mutáveis e podem conter diferentes tipos de dados.
#minha_lista = [1, 2, 3, 'Python', True]
#print("Lista original:", minha_lista)

# Adicionando um item à lista
#minha_lista.append('Novo item')
#print("Após adicionar 'Novo item':", minha_lista)

# Removendo um item da lista
#minha_lista.remove(2)  # Remove o número 2
#print("Após remover o número 2:", minha_lista)

# Acessando um item na lista
#print("Primeiro item da lista:", minha_lista[0])

# Tuplas em Python
#print("\n### Tuplas ###")
# Tuplas são semelhantes às listas, mas são imutáveis.
#minha_tupla = (10, 20, 30, 'Tupla', False)
#print("Tupla original:", minha_tupla)

# Tupla não pode ser alterada, mas podemos acessar elementos
#print("Primeiro item da tupla:", minha_tupla[0])

# Dicionários em Python
#print("\n### Dicionários ###")
# Dicionários armazenam pares de chave e valor.
#meu_dicionario = {'nome': 'João', 'idade': 22, 'cidade': 'Recife'}
#print("Dicionário original:", meu_dicionario)

# Adicionando um novo par chave-valor
#meu_dicionario['profissao'] = 'Estudante'
#print("Após adicionar 'profissao':", meu_dicionario)

# Removendo um par chave-valor
#del meu_dicionario['idade']
#print("Após remover a chave 'idade':", meu_dicionario)

# Acessando um valor no dicionário usando a chave
#print("Valor da chave 'nome':", meu_dicionario['nome'])

# Exibindo todos os pares chave-valor
#print("\nTodos os pares chave-valor no dicionário:")
#for chave, valor in meu_dicionario.items():
    #print(chave, ":", valor)


# exemplo lista

#minha_lista = [1,2,3,4,5]
#print(minha_lista[0]) # Imprime o primeiro item (1)
#print(minha_lista[1]) # Imprime o segundo item (2)

#minha_lista.append(6) # comando para adcionar um item na lista 
#print(minha_lista[5]) # Imprime o sexto item (1)

#minha_lista.remove(2) # comando para remover um item na lista nesse caso o 2
#print(minha_lista)

#minha_lista.pop() # Remove o último item
#print(minha_lista)

# exemplo dicionario 

#meu_dicionario = {"Nome": "joao", "Idade": "21", "Cidade": "Recife"}
# Você acessa os valores usando a chave correspondente. 
#print(meu_dicionario["Nome"]) # João 
#print(meu_dicionario["Idade"]) # 21

# Você pode adicionar ou atualizar valores em um dicionário usando a chave.
#meu_dicionario["Profissao"] = "Estudante" # Adicionando 
#print(meu_dicionario["Profissao"])

#meu_dicionario['idade'] = 23 # Atualizando
#print(meu_dicionario["idade"])

#del meu_dicionario["Idade"]   # Remove a chave 'idade'
#print(meu_dicionario)