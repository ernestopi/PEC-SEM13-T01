lista = list()
for cont in range(0, 10):
    lista.append(int(input()))
soma = 0
for i in lista:
    soma += i
mul = 1
for i in lista:
    mul = mul*i

print(lista)
print(soma)
print(mul)
