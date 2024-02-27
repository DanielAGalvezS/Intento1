from nodos.NodoPiso import NodoPiso
class ListaPiso:
    def __init__(self):
        self.cabeza = None

    def agregar_piso(self, piso):
        nuevo_nodo = NodoPiso(piso)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            
    def imprimir_lista(self):
        actual = self.cabeza
        print("imprimiento lista pisos")
        while actual:
            print(actual.piso.nombre, end=" ->")
            actual = actual.siguiente
        print("***********pisos*************")
