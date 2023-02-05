from conta import Conta

conta = Conta(123, "Nico", 55.5, 1000.0)
conta2 = Conta(1233, "Nico", 550.5, 1020.0)

conta.extrato()
conta2.extrato()
conta.transfere(500, conta2)
conta.extrato()
conta2.extrato()

# No Python, o "None" é parecido com o "null" do Java.
