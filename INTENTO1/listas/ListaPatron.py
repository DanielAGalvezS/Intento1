from nodos.NodoPatron import NodoPatron
class ListaPatron:
    def __init__(self):
        self.cabeza = None

    def agregar_patron(self, patron):
        nuevo_nodo = NodoPatron(patron)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def imprimir_lista(self):
        actual = self.cabeza
        print("Imprimiendo lista de patrones:")
        while actual:
            print("Código:", actual.patron.codigo, "Contenido:", actual.patron.contenido)
            actual = actual.siguiente
        print("************* Fin de la lista de patrones *************")
