from ClaseCuentaBancaria import CuentaBancaria

# ------ Ejemplo de uso ------  
cuenta = CuentaBancaria("Carlos López", 1000)

cuenta.depositar(300)
cuenta.retirar(200)
cuenta.retirar(1500)  
cuenta.mostrar_saldo()
cuenta.mostrar_movimientos()



