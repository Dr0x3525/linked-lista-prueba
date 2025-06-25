class Nodo:
    def __init__(self, dato):
        self.dato = dato # aqui se guarda el dato
        self.siguiente = None  # Puntero al siguiente nodo (inicialmente None)
        
class Lista_enlazada:
    def __init__(self):
        self.cabeza = None #puntero al primer nodo
        
    def Agregar_al_frente(self,dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        
    def agregar_al_final(self,dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        ultimo = self.cabeza
        while ultimo.siguiente:
            ultimo = ultimo.siguiente
        ultimo.siguiente = nuevo_nodo
        
    def imprimir_lista(self):
        temp = self.cabeza
        while temp:
            print(temp.dato, end=" -> ")
            temp = temp.siguiente
        print("None")
        
Lista_enlazada_1 = Lista_enlazada()
Lista_enlazada_1.Agregar_al_frente(5)
Lista_enlazada_1.Agregar_al_frente(2)
Lista_enlazada_1.agregar_al_final(2)
Lista_enlazada_1.agregar_al_final(3)
Lista_enlazada_1.agregar_al_final(3)



Lista_enlazada_1.imprimir_lista()