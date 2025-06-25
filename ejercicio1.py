"""
Implementa una Singly Linked List en Python
con los siguientes métodos:

insertar_al_inicio(dato)

insertar_al_final(dato)

eliminar(dato) (elimina la primera ocurrencia)

buscar(dato) (devuelve True si existe)

longitud() (devuelve el número de nodos)

"""

class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        
class Lista_enlazada:
    def __init__(self):
        self.cabeza = None#es la direccion al que apunta siempre al primer nodo si no esta este como va a encontrar los siguientes
        
    def insertar_al_inicio(self,dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        return 
    
    def insertar_al_final(self,dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
            return
        ultimo = self.cabeza
        while ultimo.siguiente:
            ultimo = ultimo.siguiente
        ultimo.siguiente = nuevo_nodo
            
    
    def imprimir_lista_enlazada(self):
        temp = self.cabeza
        while temp :
            print(temp.dato, end=" -> ")
            temp = temp.siguiente
        print("None")
    
    def buscar_dato(self,dato):
        temp = self.cabeza
        while temp:
            if dato == temp.dato:
                print("se encontro el dato")
                return True
            temp = temp.siguiente
        print("no se encontro el dato")
        return False

    def eliminar_dato(self,dato):
        temp = self.cabeza
        dato.anterior = None
        dato.actual = self.cabeza
        while temp:
            if dato != temp.dato:
                print(temp.dato, end=" -> ")
            temp = temp.siguiente
        print("None")
        
lista = Lista_enlazada()
lista.insertar_al_final(1)
lista.insertar_al_inicio(5)
lista.insertar_al_inicio(4)
lista.insertar_al_final(2)
lista.imprimir_lista_enlazada()
lista.buscar_dato(2)
lista.eliminar_dato(1)