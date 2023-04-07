#maior preco
precos = [100, 45, 80, 56, 200, 450, 12, 2]

maior = precos[0]

i = 0

while i <= len(precos)-1:
    valor = precos[i]
    if valor > maior:
        maior = valor
    i = i + 1

for i in range(len(precos)-1):
    valor = precos[i]
    if valor > maior:
        maior = valor

print(maior)

precos.sort()
print(precos[len(precos)-1])

precos.reverse()
print(precos[0])

#soma
precos = [100, 45, 80, 56, 200, 450, 12, 2]

soma = 0
for valor in precos:
    soma = soma + valor
print(soma)

#alturas
alturas = [1.78, 1.56, 1.50, 1.8, 2.1, 1.7]
soma = 0
for valor in alturas:
    soma = soma + valor
print(soma)

media = soma/len(alturas)
print(media)

altos = []
for valor in alturas:
    if valor > media:
        altos.append(valor)
print(altos)

#while true
while True:
    nome = input("Digite um nome: ")
    print("ola", nome)
    if(nome.upper() == "CAT"):
        break

