class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    # Com o @Property, ele executará sem o "()".
    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
