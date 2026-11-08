
class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


class NodoPostre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = None
        self.siguiente = None


class ListaPostres:
    def __init__(self):
        self.inicio = None

    # Agregar postres, permitiendo repetidos
    def agregar_postre(self, nombre):
        nuevo = NodoPostre(nombre)

        if self.inicio is None:
            self.inicio = nuevo
        else:
            actual = self.inicio

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

        return nuevo

    # Agregar ingrediente a un postre
    def agregar_ingrediente(self, postre, ingrediente):
        nuevo = NodoIngrediente(ingrediente)

        if postre.ingredientes is None:
            postre.ingredientes = nuevo
        else:
            actual = postre.ingredientes

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

    # Mostrar todos los postres y sus ingredientes
    def mostrar(self):
        actual = self.inicio

        if actual is None:
            print("La lista esta vacia.")
            return

        while actual is not None:
            print("\nPostre:", actual.nombre)

            ingrediente = actual.ingredientes

            if ingrediente is None:
                print("Sin ingredientes.")
            else:
                while ingrediente is not None:
                    print("-", ingrediente.nombre)
                    ingrediente = ingrediente.siguiente

            actual = actual.siguiente

    # Eliminar postres repetidos
    def eliminar_repetidos(self):
        actual = self.inicio

        while actual is not None:
            anterior = actual
            repetido = actual.siguiente

            while repetido is not None:

                if actual.nombre.lower() == repetido.nombre.lower():

                    # Copiar ingredientes que no existan
                    ingrediente = repetido.ingredientes

                    while ingrediente is not None:
                        encontrado = False
                        revisar = actual.ingredientes

                        while revisar is not None:
                            if revisar.nombre.lower() == ingrediente.nombre.lower():
                                encontrado = True
                                break

                            revisar = revisar.siguiente

                        if not encontrado:
                            self.agregar_ingrediente(actual, ingrediente.nombre)

                        ingrediente = ingrediente.siguiente

                    # Quitar el postre repetido
                    anterior.siguiente = repetido.siguiente
                    repetido = anterior.siguiente

                else:
                    anterior = repetido
                    repetido = repetido.siguiente

            actual = actual.siguiente


# PROGRAMA PRINCIPAL

postres = ListaPostres()

cantidad = int(input("Cuantos registros de postres deseas ingresar?: "))

for i in range(cantidad):
    print("\nRegistro", i + 1)

    nombre = input("Nombre del postre: ")
    nuevo = postres.agregar_postre(nombre)

    ingredientes = int(input("Cuantos ingredientes tiene?: "))

    for j in range(ingredientes):
        ingrediente = input("Nombre del ingrediente: ")
        postres.agregar_ingrediente(nuevo, ingrediente)

print("\n===== LISTA ORIGINAL =====")
postres.mostrar()

print("\nEliminando postres repetidos...")
postres.eliminar_repetidos()

print("\n===== LISTA SIN REPETIDOS =====")
postres.mostrar()
