def match(patron):
    print('Buscando ' + patron)
    try:
        while True:
            s = (yield)
            if patron in s:
                print(s)
    except GeneratorExit:
        print('===hecho===')