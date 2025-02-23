#Creacion de clase y metodos
class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado exitosamente. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor a cero.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Retiro de {cantidad} realizado exitosamente. Nuevo saldo: {self.saldo}")
            else:
                print("Saldo insuficiente para realizar el retiro.")
        else:
            print("La cantidad a retirar debe ser mayor a cero.")

    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

# Condiciones iniciales
saldo_inicial = float(input("Introduce el saldo inicial de la cuenta: "))

# Crear objeto
mi_cuenta = CuentaBancaria(saldo_inicial)

# instrucciones
while True:
    print("\nOpciones disponibles:")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    #switch

    if opcion == '1':
        cantidad = float(input("Introduce la cantidad a depositar: "))
        mi_cuenta.depositar(cantidad)
    elif opcion == '2':
        cantidad = float(input("Introduce la cantidad a retirar: "))
        mi_cuenta.retirar(cantidad)
    elif opcion == '3':
        mi_cuenta.consultar_saldo()
    elif opcion == '4':
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Por favor, elige una opción entre 1 y 4.")