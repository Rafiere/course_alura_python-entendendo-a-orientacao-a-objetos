def create_account(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta


def deposita(conta, valor):
    conta["saldo"] = conta["saldo"] + valor


def sacar(conta, valor):
    conta["saldo"] = conta["saldo"] - valor


def extrato(conta):
    print("O saldo é {}".format(conta["saldo"]))


conta = create_account(1234, "teste", 123, 123)

extrato(conta)
deposita(conta, 50)
extrato(conta)
sacar(conta, 25)
extrato(conta)

