def lista_a():
    la = []
    for item in range(25):
        elemento = int(input().strip())
        la.append(elemento)
    return la

def lista_b():
    lb = []
    for item in range(25):
        elemento = int(input().strip())
        lb.append(elemento)
    return lb

def nova_lista(la, lb):
    res = la + lb
    res[::2] = la
    res[1::2] = lb
    return res

def main():
    a = lista_a()
    b = lista_b()
    print(a)
    print(b)
    print(nova_lista(a, b))

if __name__ == '__main__':
    main()