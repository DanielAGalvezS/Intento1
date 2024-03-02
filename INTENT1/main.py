import xml.etree.ElementTree as ET

import graphviz

class Piso:
    def __init__(self, nombre, R, C, F, S):
        self.nombre = nombre
        self.R = R
        self.C = C
        self.F = F
        self.S = S
        self.Lista_Patrones = ListaPatron()  
        
class NodoPiso():
    def __init__(self, piso):    
        self.piso = piso
        self.siguiente = None
        
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
        lista_pisos_ordenada = sorted(self.obtener_pisos(), key=lambda piso: piso.nombre)
        
        print("Imprimiendo lista de pisos:")
        for piso in lista_pisos_ordenada:
            print("Nombre del piso:", piso.nombre)
            lista_patrones_ordenada = sorted(piso.Lista_Patrones.obtener_patrones(), key=lambda patron: patron.codigo)
            print("Patrones:")
            for patron in lista_patrones_ordenada:
                print("  Código:", patron.codigo, "Contenido:", patron.contenido)
        print("************* Fin de la lista de pisos *************")

    def obtener_pisos(self):
        pisos = []
        actual = self.cabeza
        while actual:
            pisos.append(actual.piso)
            actual = actual.siguiente
        return pisos

    def buscar_piso(self, nombre_piso):
            actual = self.cabeza
            while actual:
                if actual.piso.nombre == nombre_piso:
                    return actual.piso
                actual = actual.siguiente
            return None
        
class Patron:
    def __init__(self,codigo,contenido):
        self.codigo = codigo
        self.contenido = contenido
        
class NodoPatron():
    def __init__(self,patron):
        self.patron = patron   
        self.siguiente = None
        
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
        
    def obtener_patrones(self):
        patrones = []
        actual = self.cabeza
        while actual:
            patrones.append(actual.patron)
            actual = actual.siguiente
        return patrones
    
    def buscar_patron(self, codigo_patron):
        actual = self.cabeza
        while actual:
            if actual.patron.codigo == codigo_patron:
                return actual.patron
            actual = actual.siguiente
        return None



def CargarXML():
    #buscar el archivo XML (ubicacion)
    tree = ET.parse('entrada.xml')

    #se obtiene toda la raiza del archivo xml 
    root = tree.getroot()
    
    #iterar o recorre el elemento "pisosGuatemala" (esto se hace uno por uno)
    for piso in root.findall('piso'):
        #para obtener el nombre de la piso
        nombrePiso=piso.get('nombre')

        #se obtienen los valores de las constantes mencionadas en el enunciado
        valorR=piso.find('R').text.strip()
        valorC=piso.find('C').text.strip()
        valorF=piso.find('F').text.strip()
        valorS=piso.find('S').text.strip()
        
        miPiso = Piso(nombrePiso, valorR, valorC, valorF, valorS)
        miListaPiso.agregar_piso(miPiso)
        
        # Iterar sobre los elementos "patron" dentro de "patrones"
        for patron in piso.findall('.//patron'):
            codigo = patron.get('codigo')
            contenido = patron.text.strip()
            miPatron = Patron(codigo, contenido)
            miListaPatron.agregar_patron(miPatron)
            miPiso.Lista_Patrones.agregar_patron(miPatron)
          
            
def Menu():
    while True:
        print('-------------------------------------------------')
        print('escoja una opcion')
        print('1. mostar pisos disponibles ordenados en orden alfabetico')
        print('2. Graficar un piso con un patron especifico')
        print('3. cerrar')
        entrada=input()
        if(entrada == '1'):
            print('-------CARGANDO TODOS LOS PISOS-------')
            miListaPiso.imprimir_lista()
            
        elif(entrada == '2'):
            print('----Se ha creado un archivo PNG del piso con un patron especifico')
            nombre_piso = input('Ingrese el nombre del piso: ')
            codigo_patron = input('Ingrese el código del patrón: ')

            
            piso_existente = miListaPiso.buscar_piso(nombre_piso)

            if piso_existente:
                
                patron_existente = piso_existente.Lista_Patrones.buscar_patron(codigo_patron)
                if patron_existente:
                    contenido = patron_existente.contenido
                    matrix_grafo = crear_matrix(int(piso_existente.R),int(piso_existente.C),contenido)
                    matrix_grafo.render('matrix_grafo', format='png', cleanup=True)
                    matrix_grafo.view()

                else:
                    print('El piso existe pero el patrón no pertenece a ese piso.')
            else:
                print('El piso ingresado no existe en el sistema.')    
        elif(entrada == '3'):
            print('-------Gracias por usar el software-------')
            break
        else:
            print('opcion ingresada incorrecta')








def crear_matrix(filas, columnas, contenido):
    assert len(contenido) == filas * columnas, "El contenido del patron debe coincidir con el tamaño de la matriz"
    
    dot = graphviz.Graph(format='png', graph_attr={'rankdir': 'TB'})  
    
    for i in range(filas):
        with dot.subgraph() as s:  
            s.attr(rank='same')  
            for j in range(columnas):
                color = 'black' if contenido[i * columnas + j] == 'N' else 'white'
                s.node(f'{i}{j}', style='filled', fillcolor=color, shape='square')
    
   
    for i in range(filas):
        for j in range(columnas):
            if j < columnas - 1:
                dot.edge(f'{i}{j}', f'{i}{j+1}')
            if i < filas - 1:
                dot.edge(f'{i}{j}', f'{i+1}{j}')
    
    return dot



miListaPiso = ListaPiso()
miListaPatron = ListaPatron()
CargarXML()
Menu()