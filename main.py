from app.db.dbConn import create_tables
from app.controllers.UserController import crear_usuario
from app.controllers.CuentaController import crear_cuenta, actualizar_saldo_cuenta
from app.controllers.TarjetaController import crear_tarjeta, procesar_gasto_tarjeta, procesar_deposito_tarjeta
def main():
    create_tables()
    usuario1 = crear_usuario("Juan")
    cuenta1 = crear_cuenta(usuario1, 1000.00)
    tarjeta1 = crear_tarjeta(cuenta1, 1000.00)

    print("Saldo inicial de la tarjeta:", tarjeta1.balance)
    procesar_deposito_tarjeta(tarjeta1, 500.00)
    print("Saldo después del depósito:", tarjeta1.balance)

    try:
        procesar_gasto_tarjeta(tarjeta1, 700.00)
        print("Gasto realizado exitosamente.")
    except ValueError as e:
        print(str(e))

    actualizar_saldo_cuenta(cuenta1)
    print("Saldo actualizado de la cuenta:", cuenta1.saldo)

if __name__ == '__main__':
    main()
