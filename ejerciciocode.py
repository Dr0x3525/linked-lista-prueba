# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def obtener_listas_invertidas(self,lis):
        lista = []
        while lis:
            lista.append(lis.val)
            lis = lis.next
        lista.reverse()
        return lista

    def convertir_lista_en_numero(self,li):
        num = ""
        for numero in li:
            numero = str(numero)
            num += numero
        num = int(num)
        return num


    def convertir_numero_en_lista(self,numero):
        lista_digitos = [int(digito) for digito in str(numero)]
        return lista_digitos

    def lista_a_enlazada(self,lista):
        if not lista:
            return None
        
        cabeza = ListNode(lista[0])
        actual = cabeza
        
        for valor in lista[1:]:
            actual.next = ListNode(valor)
            actual = actual.next
        
        return cabeza

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        lista1 = self.obtener_listas_invertidas(l1)
        lista2 = self.obtener_listas_invertidas(l2)
        numero1 = self.convertir_lista_en_numero(lista1)#convertir en numeros
        numero2 = self.convertir_lista_en_numero(lista2)
        resultado = numero1 + numero2 #obtiene el resultado
        resultado = self.convertir_numero_en_lista(resultado)#convierte en lista
        resultado.reverse()
        lista_enlazada = self.lista_a_enlazada(resultado)
        return lista_enlazada
