import datetime

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.movimientos = []  # Lista de tuplas: (fecha, tipo, monto, saldo)

    def depositar(self, monto):
        # Completar lo siguiente: 
        # 1. actualizar saldo
        self.saldo += monto 
        # 2. añadir movimiento de deposito (fecha, tipo, monto, saldo) 
        fecha = datetime.datetime.now()
        datosMov = (fecha, "deposito", monto, self.saldo)
        self.movimientos.append(datosMov)
        # 3. Mostrar mensaje de depósito exitoso
        print(f"deposito exitoso: {datosMov}")
        pass

    def retirar(self, monto):
        # Completar lo siguiente: 
        # 1. Validar saldo, y si es insuficiente mostrar mensaje
        if self.saldo < monto:
            print('no hay saldo suficiente')
        # 2. Actualizar saldo
        else:
            self.saldo -= monto    
        # 3. Añadir movimiento de retiro (fecha, tipo, monto, saldo)
            fecha = datetime.datetime.now()
            datosMov = (fecha, "retiro", monto, self.saldo)
            self.movimientos.append(datosMov)
        # 4. Mostrar mensaje de retiro exitoso
        print(f"retiro exitoso: {datosMov}")
        pass

    def mostrar_saldo(self):
        # Completar lo siguiente: 
        # 1. mostrar mensaje con nombre de titular y su saldo.
        print(f"titular: {self.titular}, saldo: {self.saldo}")
        pass

    def mostrar_movimientos(self):
        print(f"\n--- Historial de {self.titular} ---")
        # Completar lo siguiente: 
        # 1. iterar la lista de movimientos y mostar la fecha, tipo el monto y el saldo.
        for movimiento in self.movimientos:
            print(f'fecha: {movimiento[0]}')
            print(f'tipo: {movimiento[1]}')
            print(f'monto: {movimiento[2]}')
            print(f'saldo: {movimiento[3]}')
        pass


