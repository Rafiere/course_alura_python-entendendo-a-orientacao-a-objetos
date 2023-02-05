class Conta:

    def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

    def __str__(self):
        return f"Conta número: {self.numero}, titular: {self.titular}, saldo: {self.saldo}, limite: {self.limite}"

    # A função "init" é uma função construtora.
    # O "self" é a referência que sabe encontrar o objeto que está sendo construído nessa função.
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
