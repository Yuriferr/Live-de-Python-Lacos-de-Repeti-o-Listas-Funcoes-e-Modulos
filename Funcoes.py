def precos(precos):
    maior = precos[0]
    i = 0

    for i in range(len(precos) - 1):
        valor = precos[i]
        if valor > maior:
            maior = valor

    return maior

print(precos([100, 45, 80, 56, 200, 450, 12, 2]))

def somar(numeros):
    soma = 0

    for valor in numeros:
        soma = soma + valor

    return soma

print(somar([1, 2, 3, 4, 5]))

def aluras(alturas):
    soma = 0

    for valor in alturas:
        soma = soma + valor

    media = soma / len(alturas)

    altos = []

    for valor in alturas:
        if valor > media:
            altos.append(valor)

    return soma, media, altos

print(aluras([1.78, 1.56, 1.50, 1.8, 2.1, 1.7]))