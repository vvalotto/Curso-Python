import asyncio

@asyncio.coroutine
def saludar_cada_dos_segundos():
    while True:
        print("Hola Mundo")
        yield from asyncio.sleep(2)

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(saludar_cada_dos_segundos())
finally:
    loop.close()