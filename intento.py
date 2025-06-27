class nodo:
    def __init__(self,dato):
        self.dato = dato 
        self.puntero = None

class linked_list:
#entendi hasta aqui
    def __init__(self):
        self.cabeza = None
    
    def agregar_un_nodo_al_inicio(self,dato):
        nuevo_nodo = nodo(dato)
        nuevo_nodo.puntero = self.cabeza
        self.cabeza = nuevo_nodo
    
    def agregar_un_nodo_al_final(self,dato):
        nuevo_nodo = nodo(dato)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
        else:
            temp = self.cabeza
            while temp.puntero != None:
                temp = temp.puntero
            temp.puntero = nuevo_nodo
                
    def mostrar_la_lista(self):    
        temp = self.cabeza
        while temp.puntero != None:
            print(temp.dato, end="-")
            temp = temp.puntero
        print("None")
        
        
lista_enlazada = linked_list()
lista_enlazada.agregar_un_nodo_al_inicio(2)
lista_enlazada.agregar_un_nodo_al_inicio(3)
lista_enlazada.agregar_un_nodo_al_inicio(4)
lista_enlazada.agregar_un_nodo_al_inicio(5)
lista_enlazada.agregar_un_nodo_al_inicio(3)
lista_enlazada.agregar_un_nodo_al_final(100)
lista_enlazada.agregar_un_nodo_al_final(200)


lista_enlazada.mostrar_la_lista()
