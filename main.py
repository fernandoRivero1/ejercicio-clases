from ClaseCuentaBancaria import CuentaBancaria

# ------ Ejemplo de uso ------  
cuenta = CuentaBancaria("Carlos López", 1000)

# print(cuenta.titular)
# print(cuenta.saldo)
# print(cuenta.movimientos)
# print('---------')
cuenta.depositar(300)
# print('---------')
# print(cuenta.titular)
# print(cuenta.saldo)
# print(cuenta.movimientos)
# print('---------')
cuenta.retirar(200)
# print('---------')
# print(cuenta.titular)
# print(cuenta.saldo)
# print(cuenta.movimientos)


cuenta.retirar(1500)  
cuenta.mostrar_saldo()
cuenta.mostrar_movimientos()

cuenta2 = CuentaBancaria('fabian', 1500)
cuenta2.depositar(100)
cuenta2.retirar(800)
cuenta2.mostrar_saldo()
cuenta2.mostrar_movimientos()
