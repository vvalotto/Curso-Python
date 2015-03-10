class Proceso(object):

    def __init__(self):
        self._nombre = ""
        self._codigo = ""
        pass

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor


    @property
    def codigo(self):
        return self._codigo

    @nombre.setter
    def codigo(self, valor):
        self._codigo = valor

