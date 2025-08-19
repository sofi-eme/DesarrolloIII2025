# Sofy Moncada y lu Palacios
from objeto import Impresora
##hi
def mostrar_menu():
    print("\n Menú de la Impresora ")
    print("2. Apagar impresora")
    print("3. Agregar documento a la cola")
    print("4. Imprimir documento")
    print("5. Ver estado de la impresora")
    print("6. Salir")

def main():
    impresora = Impresora("HP", "DeskJet 2700", 10)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            print(impresora.encender())
        elif opcion == "2":
            print(impresora.apagar())
        elif opcion == "3":
            doc = input("Nombre del documento: ")
            print(impresora.agregar_documento(doc))
        elif opcion == "4":
            print(impresora.imprimir())
        elif opcion == "5":
            print(impresora)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
