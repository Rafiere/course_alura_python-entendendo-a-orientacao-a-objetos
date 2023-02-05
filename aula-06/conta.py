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

    def pode_sacar(self):
        if self.__saldo <= 0.00:
            print("Não pode sacar!")

    @staticmethod
    def codigo_banco(self):
        return "001"

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def __str__(self):
        return f"Conta número: {self.__numero}, titular: {self.__titular}, saldo: {self.__saldo}, limite: {self.__limite}"

    # A função "init" é uma função construtora.
    # O "self" é a referência que sabe encontrar o objeto que está sendo construído nessa função.
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
