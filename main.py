"""
Spanish: Modulo para manipulación de los elementos de una lista

Lleva a cabo la modificación de posiciones de una lista
Este modulo esta constituido por una clase y una función que permiten invertir la posición de los elementos de una lista

Funciones Disponible:
- list_inverter: Invierte la posición de los elementos de una lista que es entregada como su argumento.

Clases Disponibles:
- ListHandler: Clase para realizar al manipulación de la posición de los elementos de una lista

------------

English:

"""

class ListHandler:
    """ Clase para realizar la manipulación de la posición de los elementos de una lista

    Esta clase contiene un metodo que permite realizar la inversión de la posición de los elementos
    de una lista que se le entrega como argumento.
    """

    def list_inverter(self, original_list:list) -> list:
        """ Invierte las posiciones de los elementos de la lista

        Esta función toma la lista que es entregada como argumento e invierte la posición de sus elementos.
        
        Args:
            - original_list (list): Lista que se desea invertir

        Returns:
            - list: Lista invertida

        Constrains:
            - La función no permite procesar listas vacias.
            - La función no procesa tipos de datos diferentes a listas
        """

        if type(original_list)!=list:
            raise TypeError("El dato ingresado no es de tipo Lista")
        
        elif len(original_list)<1:
            raise ValueError("La lista está vacia")
        
        else:
            inverted_list =  original_list[::-1]
            return inverted_list



#if __name__ == "__main__":

 #   separator = str(input("ingrese el separador que desea usar en la lista: ")) or ","
 #   user_list = input(f"Ingrese una lista cuyo separador sea: {separator} ").split(separator)

 #   new_obj = ListHandler()
 #   inverted_list = new_obj.list_inverter(original_list=user_list)

 #  print(f"Original List: {user_list}")
 #   print(f"Inverted List: {inverted_list}")
