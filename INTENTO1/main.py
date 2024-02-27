import xml.etree.ElementTree as ET
from modelo.piso import Piso
from modelo.patron import Patron
from listas.ListaPatron import ListaPatron
from listas.ListaPiso import ListaPiso

miListaPiso = ListaPiso()
miListaPatron = ListaPatron()

def CargarXML():
    #buscar el archivo XML (ubicacion)
    tree = ET.parse('entrada.xml')

    #se obtiene toda la raiza del archivo xml 
    root = tree.getroot()
    
    #iterar o recorre el elemento "pisosGuatemala" (esto se hace uno por uno)
    for piso in root.findall('piso'):
        print("___________________________________________________________")
        #para obtener el nombre de la piso
        nombrePiso=piso.get('nombre')

        #se obtienen los valores de las constantes mencionadas en el enunciado
        valorR=piso.find('R').text.strip()
        valorC=piso.find('C').text.strip()
        valorF=piso.find('F').text.strip()
        valorS=piso.find('S').text.strip()
        
        miPiso = Piso(nombrePiso,valorR,valorC,valorF,valorS,None)
        miListaPiso.agregar_piso(miPiso)
        '''
        print("Nombre del Piso: ", nombrePiso)
        print("R: ", valorR)
        print("C: ", valorC)
        print("F: ", valorF)
        print("S: ", valorS)
        '''
        # Iterar sobre los elementos "patron" dentro de "patrones"
        for patron in piso.findall('.//patron'):
            codigo = patron.get('codigo')
            contenido = patron.text.strip()
            miPatron=Patron(codigo,contenido)
            miListaPatron.agregar_patron(miPatron)  
            #print("     Patron:", codigo, "Contenido: ", contenido)
            
            '''
            print('MI listass')
            # Imprimir los patrones almacenados en la lista enlazada
            actual = lista_patrones.cabeza
            while actual:
                print("Patron:", actual.codigo, "Contenido:", actual.contenido)
                actual = actual.siguiente
            '''
          
            
def Menu():
    while True:
        print('-------------------------------------------------')
        print('escoja una opcion')
        print('1. mostar pisos disponibles')
        print('2. cerrar')
        entrada=input()
        if(entrada == '1'):
            print('-------CARGANDO TODOS LOS PISOS-------')
            CargarXML()
            miListaPiso.imprimir_lista()
            miListaPatron.imprimir_lista()
            Menu()
        if(entrada == '2'):
            print('-------Gracias por usar el software-------')
            break
        else:
            print('opcion ingresada incorrecta')
            
Menu()        