def listagem():
    x = int(input().strip())
    a = []
    b = []
    c = []
    e = 0
    g = 0

    for i in range(x):
        a.insert(0, round(float(input().strip()), 4))
    print(a)

    for i in range(x):
        b.append(round(float(input().strip()), 1))
        e += b[i]
    print(b)
    if e == 0:
        print('sem notas')
    else:
        print(round((e / x), 1))

    for i in range(x):
        f = input().strip()
        if f in 'aeiouAEIOU':
            g += 1

        if f in 'BCDFGHJKLMNPQRSTVXYZbcdfghjklmnpqrstvxyz':
            c.append(f)
        print(g)
        print(c)

def main():
    listagem()

if __name__ == '__main__':
    main()