# 1 - Algoritmo para dizer quantos números pares, múltiplos de 47 e 37 existem
# no intervalo de 1 a 5 * 10^6
print("\n\n\n\n-------------- Exercicio 1 ------------------")

counter = 0
for x in range(1, 5 * pow(10, 6) + 1):
    if ((x % 2 == 0) and (x % 37 == 0) and (x % 47 == 0)):
        counter += 1

print("Contagem: ", counter)
# resposta: 1437


# *********************************************** #
print("\n\n\n\n-------------- Exercicio 2 ------------------")

# 2 - Criar um vetor com 10 posições. Sendo i a posição de um elemento no vetor,
# Preencher com 3^(i) + 7 * (i!). Se i for ímpar, preencher a posição com 
# 2^i + 4 * ln(i), onde "ln" é o logaritmo neperiano.

from math import log
from math import factorial

vector = []
max_value = 0
max_index = 0
for index in range (0, 10):
    if (index % 2 == 0):
        vector.append(pow(3, index) + 7 * factorial(index))

        # Para não percorrer o vetor duas vezes, já
        # vejo qual o maior valor no loop
        if (max_value < vector[index]):
            max_value = vector[index]
            max_index = index;
    else:
        vector.append(pow(2, index) + 4 * log(index))
        if (max_value < vector[index]):
            max_value = vector[index]
            max_index = index;


# Uma vez preenchido o vetor, deseja-se saber qual a posição do maior
# elemento e qual a média de todos os elementos 
print ("Posição do maior elemento (de 0 a 9): ", max_index, ", cujo valor é ", max_value)
print ("Média: ", round(sum(vector)/len(vector), 2))

# Resultado:
# Posição do maior elemento (de 0 a 9):  8 , cujo valor é  288801
# Média:  29555.94


# *********************************************** #
print("\n\n\n\n-------------- Exercicio 3 ------------------")
# Fazer um algoritmo que leia a nota de 5 alunos e uma nota para cada
# aluno. Guardar a informação em um dicionário e apresentar a maior nota

alunos = {
    "aluno1": 0,
    "aluno2": 0,
    "aluno3": 0,
    "aluno4": 0,
    "aluno5": 0
}
for index in range(5):
    nota = input("Qual a nota do " + str(index + 1) + "o aluno? ")
    alunos["aluno" + str(index)] = int(nota)

# melhor_nota guarda o melhor aluno na posição 0 e a melhor nota na
# posição 1
melhor_nota = ["nome_aluno", 0]
for myList in alunos.items():
    if (melhor_nota[1] < myList[1]):
        melhor_nota[1] = myList[1]
        melhor_nota[0] = myList[0]

print("A melhor nota foi", melhor_nota[1], ", de", melhor_nota[0])
