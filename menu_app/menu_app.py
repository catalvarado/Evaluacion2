
def agregar_compra(lista, compra):
    lista.append(compra)
    print("La compra se ha agregado correctamente")


def mostrar_compras(lista):
    if len(lista) == 0:
        print("No hay compras registradas")
    else:
        for indice, compra in enumerate(lista):
            print(f"{indice}: ${compra}")


def mostrar_total(lista, total):
    for i in lista:
        total += i
    total_redodeado = round(total, 2)
    print(f"Total gastado: ${total_redodeado}")


def main():
    compras = []
    total_gastado = 0

    while True:
        print("Menú: \n1.Agregar una compra \n2. Mostrar compras \n3. Mostrar total gastado \n4. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            monto = int(input("Ingrese el monto de la compra: "))
            agregar_compra(compras, monto)
        elif opcion == 2:
            mostrar_compras(compras)
        elif opcion == 3:
            mostrar_total(compras, total_gastado)
        elif opcion == 4:
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


main()
