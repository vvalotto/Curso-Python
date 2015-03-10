import sys

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("Error: ", sys.exc_info()[0])
        raise ValueError("Mal ingreso")
print("Great, you successfully entered an integer!")