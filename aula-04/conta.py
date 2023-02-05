class Conta:

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def __str__(self):
        return f"Conta número: {self.__numero}, titular: {self.__titular}, saldo: {self.__saldo}, limite: {self.__limite}"

    # A função "init" é uma função construtora.
    # O "self" é a referência que sabe encontrar o objeto que está sendo construído nessa função.
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
