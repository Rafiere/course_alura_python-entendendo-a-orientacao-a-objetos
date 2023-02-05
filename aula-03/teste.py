from conta import Conta

conta = Conta(123, "Nico", 55.5, 1000.0)

conta.extrato()
conta.deposita(500)
conta.extrato()
conta.saca(100)
conta.extrato()

# No Python, o "None" é parecido com o "null" do Java.
