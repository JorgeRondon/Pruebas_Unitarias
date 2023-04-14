""" Español: Modulo para realizar pruebas unitarias de la función list_inverter de la clase ListHandler

        Lleva a cabo un conjunto de pruebas unitarias haciendo uso del framework pytest
        
        Funciones Disponibles:
            - test_inverter: Prueba que la inversión de una lista se haga de forma correcta
            - test_invalid_datatype: Prueba que la función no procesa tipos de datos diferentes a listas.
            - test_void_list: Prueba que la función no procesa listas vacias

    English: Module to perform unit tests of the list_inverter function of the ListHandler class.

        Performs a set of unit tests using the pytest framework.
        
        Available functions:
            - test_inverter: Tests that the inversion of a list is done correctly.
            - test_invalid_datatatype: Tests that the function does not process data types other than lists.
            - test_void_list: Tests that the function does not process empty lists.
"""


import pytest
from Pruebas_Unitarias.main import ListHandler

@pytest.mark.parametrize(
        "lista, expected",
        [
            ([1,"Hola", True,None,6],[6,None,True,"Hola",1]),
            ([None,None,None],[None,None,None])
        ]
)
def test_inverter(lista: list, expected: list) -> None:
    """ Español: Prueba que la inversión de una lista se haga de forma correcta y que procesa datos de tipo lista.

        Args:
            lista (list): lista a invertir
            expected (list): Lista invertida que se espera recibir como retorno.

        English: Tests that the inversion of a list is done correctly and that it processes data of type list.

        Args:
            list (list): list to invert.
            expected (list): inverted list expected to receive as return.
    
    """
    my_obj = ListHandler()
    assert my_obj.list_inverter(original_list=lista) == expected


@pytest.mark.parametrize(
    "lista",
    [
        (None),
        (3),
        ({"my_key":"my_value"}),
        ((1,2,3,[1,2,3]))
    ]
)
def test_invalid_datatype(lista:any)->None:
    """ Español: Prueba que la función no procesa tipos de datos diferentes a listas.

        Args:
            lista (any): Cualquier tipo de dato.

        English: Tests that the function does not process data types other than lists.

        Args:
            list (any): any data type.
    
    """
    my_obj = ListHandler()
    with pytest.raises(TypeError, match="El dato ingresado no es de tipo Lista"):
        my_obj.list_inverter(original_list=lista)


@pytest.mark.parametrize(
        "lista",
        [
            ([])
        ]
)
def test_void_list(lista:list)-> None:
    """ Español: Prueba que la función no procesa listas vacias.

        Args:
            lista (list): Lista vacia

        English: Tests that the function does not process empty lists.

        Args:
            list (list): Empty list
    
    """
    my_obj = ListHandler()
    with pytest.raises(ValueError, match="La lista está vacia"):
        my_obj.list_inverter(original_list=lista)
