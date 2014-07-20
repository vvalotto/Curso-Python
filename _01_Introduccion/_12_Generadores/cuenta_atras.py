def cuenta_atras(n):
    print("Contando para atras")
    while n > 0:
        yield n
        n -= 1
