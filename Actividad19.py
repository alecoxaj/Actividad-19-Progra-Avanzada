class RegistroDuplicadoError(Exception):
    pass


class Galleta:
    def __init__(self, nombre, precio, peso):
        if nombre == "":
            raise ValueError("El nombre no puede estar vacío.")
        if precio <= 0:
            raise ValueError("El nombre debe ser mayor que 0")
        if peso <= 0:
            raise ValueError("El peso debe ser mayor que 0")
        self.nombre = nombre
        self.precio = precio
        self.peso = peso

    def mostrar_info(self):
        return f"Nombre: {self.nombre} | Precio: {self.precio:.2f} | Peso: {self.peso}g"


class GalletaChispas(Galleta):
    def __init__(self, nombre, precio, peso, cantidad_chispas):
        Galleta.__init__(self, nombre, precio, peso)
        if cantidad_chispas < 0:
            raise ValueError("La cantidad de chispas no puede ser negativa.")
        self.cantidad_chispas = cantidad_chispas

    def mostrar_info(self):
        return Galleta.mostrar_info(self) + f" | Chispas: {self.cantidad_chispas}"


class Relleno:
    def __init__(self, sabor_relleno):
        if sabor_relleno == "":
            raise ValueError("El sabor del relleno no puede ser vacío.")
        self.sabor_relleno = sabor_relleno

    def describir_relleno(self):
        return f"Relleno: {self.sabor_relleno}"


class GalletaRellena(Galleta, Relleno):
    def __init__(self, nombre, precio, peso, sabor_relleno):
        Galleta.__init__(self, nombre, precio, peso)
        Relleno.__init__(self, sabor_relleno)

    def mostrar_info(self):
        return Galleta.mostrar_info(self) + f" | {self.describir_relleno()}"


inventario = []


def pedir_numero(mensaje, tipo=float):
    while True:
        try:
            valor = tipo(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Intenta nuevamente.")


def galleta_existe(nombre):
    for g in inventario:
        if g.nombre == nombre:
            return True
    return False


def registrar_galleta():
    try:
        nombre = input("Ingresa el nombre: ")
        if galleta_existe(nombre):
            raise RegistroDuplicadoError("Ya existe una Galleta con ese nombre.")
        precio = pedir_numero("Ingresa el precio: ")
        peso = pedir_numero("Ingresa el peso (g): ")
        g = Galleta(nombre, precio, peso)
        inventario.append(g)
        print("¡Tu galleta ha sido registrada correctamente!")
    except (ValueError, RegistroDuplicadoError) as e:
        print(f"¡ERROR! {e}")


def registrar_galleta_con_chispas():
    try:
        nombre = input("Ingresa el nombre: ")
        if galleta_existe(nombre):
            raise RegistroDuplicadoError("Ya existe una Galleta con ese nombre.")
        precio = pedir_numero("Ingresa el precio: ")
        peso = pedir_numero("Ingresa el peso (g): ")
        chispas = pedir_numero("Ingresa la cantidad de chispas: ", int)
        g = GalletaChispas(nombre, precio, peso, chispas)
        inventario.append(g)
        print("¡Tu galleta con chispas ha sido registrada correctamente!")
    except (ValueError, RegistroDuplicadoError) as e:
        print(f"¡ERROR! {e}")


def registrar_galleta_rellena():
    try:
        nombre = input("Ingresa el nombre: ")
        if galleta_existe(nombre):
            raise RegistroDuplicadoError("Ya existe una Galleta con ese nombre.")
        precio = pedir_numero("Ingresa el precio: ")
        peso = pedir_numero("Ingresa el peso (g): ")
        sabor_relleno = input("Ingresa el sabor de relleno: ")
        g = GalletaRellena(nombre, precio, peso, sabor_relleno)
        inventario.append(g)
        print("¡Tu galleta rellena ha sido registrada correctamente!")
    except (ValueError, RegistroDuplicadoError) as e:
        print(f"¡ERROR! {e}")


def listar_galleta():
    for g in inventario:
        print(g.mostrar_info())


def buscar_galletas():
    nombre = input("Ingresa el nombre: ")
    encontrados = [g for g in inventario if g.nombre == nombre]
    if encontrados:
        for g in encontrados:
            print(g.mostrar_info())
    else:
        print("No se encontró tu galleta.")


def eliminar_galleta():
    nombre = input("Ingresa el nombre para eliminar: ")
    for g in inventario:
        if g.nombre == nombre:
            inventario.remove(g)
            print("Tu galleta ha sido eliminada exitosamente.")
            return
    print("No se encontró tu galleta.")


while True:
    print("MENÚ: ")
    print("1. Registrar galleta básica")
    print("2. Registrar galleta con chispas")
    print("3. Registrar galleta rellena")
    print("4. Listar galleta")
    print("5. Buscar por nombre")
    print("6. Eliminar por nombre")
    print("7. Salir")

    option = input("Ingresa una opción (1-7): ")

    match option:
        case "1":
            registrar_galleta()
        case "2":
            registrar_galleta_con_chispas()
        case "3":
            registrar_galleta_rellena()
        case "4":
            listar_galleta()
        case "5":
            buscar_galletas()
        case "6":
            eliminar_galleta()
        case "7":
            print("¡Programa finalizado! Saliendo...")
            break

        case _:
            print("Opción no válida. Inténtalo nuevamente.")
