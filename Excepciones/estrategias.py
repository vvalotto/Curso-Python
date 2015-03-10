import sys

def volcar():
    raise RuntimeError('Este es un mensaje de error')

def ppal():
    try:
        volcar()
        return 0
    except Exception as err:
        print(str(err))
        return 1

if __name__ == '__main__':
    sys.exit(ppal())