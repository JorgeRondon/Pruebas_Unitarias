"""
Español: Modulo para manipulación de los elementos de una lista

    Lleva a cabo la modificación de posiciones de una lista
    Este modulo esta constituido por una clase y una función que permiten invertir la posición de los elementos de una lista

    Funciones Disponible:
    - list_inverter: Invierte la posición de los elementos de una lista que es entregada como su argumento.

    Clases Disponibles:
    - ListHandler: Clase para realizar al manipulación de la posición de los elementos de una lista

English: Module to manipulate list elements.

    Modify the element positions of a list.
    This module consists of a class and a function that allow to invert the position of a list elements.

    Available Functions:
    - list_inverter: Inverts the position of the elements of a list that is given as its argument.

    Available Classes:
    - ListHandler: Class to manipulate the position of the list elements.

"""

class ListHandler:
    """ Español: Clase para realizar la manipulación de la posición de los elementos de una lista

            Esta clase contiene un metodo que permite realizar la inversión de la posición de los elementos
            de una lista que se le entrega como argumento.

        English: Class to manipulate the position of the elements of a list.

            This class contains a method that allows to invert the position of the elements of a list given as an argument.
    """
    #def __init__(self):
        #self.or_list = None

    def list_inverter(self, original_list:list) -> list:
        """ Español: Invierte las posiciones de los elementos de la lista

                Esta función toma la lista que es entregada como argumento e invierte la posición de sus elementos.
                
                Args:
                    - original_list (list): Lista que se desea invertir

                Retorno:
                    - list: Lista invertida

                Restricciones:
                    - La función no permite procesar listas vacias.
                    - La función no procesa tipos de datos diferentes a listas

            English: Inverts the position of the elements of a list.

                This function takes the list that is given as an argument and inverts the position of its elements.
                
                Args:
                    - original_list (list): Lista to invert

                Returns:
                    - invereted_list (list): inverted list

                Constrains:
                    - Function does not allow empty lists.
                    - Function just process list datatypes.
        """

        if type(original_list)!=list:
            raise TypeError("El dato ingresado no es de tipo Lista")
        
        elif len(original_list)<1:
            raise ValueError("La lista está vacia")
        
        else:
            inverted_list =  original_list[::-1]
            self.or_list = inverted_list
            return inverted_list


#Script para ejecutar este modulo desde consola:
#if __name__ == "__main__":

 #   separator = str(input("ingrese el separador que desea usar en la lista: ")) or ","
 #   user_list = input(f"Ingrese una lista cuyo separador sea: {separator} ").split(separator)

 #   new_obj = ListHandler()
 #   inverted_list = new_obj.list_inverter(original_list=user_list)

 #   print(f"Original List: {user_list}")
 #   print(f"Inverted List: {inverted_list}")
 #   print(f"or_list atribute: {new_obj.or_list}")
