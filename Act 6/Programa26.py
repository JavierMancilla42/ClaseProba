class Agenda:    #Creaciin de clase y funciones
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono, correo):
        self.contactos[nombre] = {"telefono": telefono, "correo": correo}
        print(f"Contacto {nombre} agregado correctamente.")

    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            for nombre, info in self.contactos.items():
                print(f"Nombre: {nombre}, Teléfono: {info['telefono']}, Correo: {info['correo']}")

    def buscar_contacto(self, nombre):
        if nombre in self.contactos:
            info = self.contactos[nombre]
            print(f"Nombre: {nombre}, Teléfono: {info['telefono']}, Correo: {info['correo']}")
        else:
            print("Contacto no encontrado.")

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            print(f"Contacto {nombre} eliminado correctamente.")
        else:
            print("Contacto no encontrado.")

agenda = Agenda()    #Creacion de objeto
while True:
    print("\n1. Agregar contacto")    #Instrucciones
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":    #Switch
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        agenda.agregar_contacto(nombre, telefono, correo)
    elif opcion == "2":
        agenda.mostrar_contactos()
    elif opcion == "3":
        nombre = input("Ingrese el nombre a buscar: ")
        agenda.buscar_contacto(nombre)
    elif opcion == "4":
        nombre = input("Ingrese el nombre a eliminar: ")
        agenda.eliminar_contacto(nombre)
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")