def par_impar():
    lista = []
    par = []
    impar = []
    for item in range(20):
        elemento = int(input().strip())
        lista.append(elemento)
        if elemento % 2 == 0:
            par.append(elemento)
        else:
            impar.append(elemento)
    print(f'{lista}\n{par}\n{impar}')

def main():
    par_impar()

if __name__ == '__main__':
    main()