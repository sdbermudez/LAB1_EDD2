import os
import pandas as pd
from typing import Any, Optional, Tuple
import networkx as nx
import matplotlib.pyplot as plt

# Obtener la ruta absoluta del archivo
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'dataset_movies.csv')

# Leer el archivo CSV
data = pd.read_csv(file_path)
print(data.head())
   
#Funcion para mostrar el menu inicial, donde se le pregunta al usuario cuantas peliculas desea cargar y como desea cargarlas 
def menu_inicial():
    print("Cuantas peliculas desea cargar?")
    numPeliculas=int(input())
    print("Como desea cargar las peliculas al arbol?")
    print("1. Cargar por nombre")
    print("2. Cargar por indice")
    print("3. Cargar por año")
    print("4. salir")
    op=0
    while op<1 or op>4:
        op=int(input("Ingrese la opcion deseada: "))
    return op, numPeliculas

#Funcion para crear el arbol AVL
def crear_arbol(listaPeliculas):
    for pelicula in listaPeliculas:
        arbol.insert(pelicula)
    return arbol

#Funcion para mostrar el arbol graficamente
def graficar_arbol(arbol):
    G = nx.DiGraph()
    cola = [arbol.root]
    while cola:
        nodo = cola.pop(0)
        if nodo.left:
            cola.append(nodo.left)
            G.add_edge(nodo.data['Title'], nodo.left.data['Title'])
        if nodo.right:
            cola.append(nodo.right)
            G.add_edge(nodo.data['Title'], nodo.right.data['Title'])
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue')
    plt.show()
    
#Funcion que carga las peliculas a una lista de diccionarios teniendo en cuenta el nombre de la pelicula
def cargar_nombre(numPeliculas, data): 
    listaPeliculasN = []
    for i in range(numPeliculas):
        nombre=input(f"Escriba el nombre de la pelicula {i + 1}: ")
        pelicula = data[data['Title'].str.upper() == nombre.upper()]
        if not pelicula.empty:
            listaPeliculasN.append(pelicula.iloc[0].to_dict())
        while pelicula.empty:
            print(f"No se encontró la película con el nombre '{nombre}'")
            nombre=input(f"Escriba el nombre de la pelicula {i + 1}: ")
            pelicula = data[data['Title'].str.upper() == nombre.upper()]
            if not pelicula.empty:
                listaPeliculasN.append(pelicula.iloc[0].to_dict())
    return listaPeliculasN

#Funcion que carga las peliculas a una lista de diccionarios teniendo en cuenta el indice de la pelicula dentro del dataset
def cargar_indice(numPeliculas, data):
    listaPeliculasI = []
    for i in range(numPeliculas):
        print("Escriba el indice de la pelicula ", i + 1)
        indice = int(input())
        if indice >= 0 and indice < len(data):
            listaPeliculasI.append(data.iloc[indice].to_dict())
        else:
            print(f"No se encontró la película con el índice '{indice}'")
    return listaPeliculasI

#Funcion que carga las peliculas a una lista de diccionarios teniendo en cuenta el año de la pelicula
def cargar_anio(numPeliculas, data):
    listaPeliculasA = []
    for i in range(numPeliculas):
        print("Escriba el año de la pelicula ", i + 1)
        anio = int(input())
        pelicula = data[data['Year'] == anio]
        if not pelicula.empty:
            listaPeliculasA.append(pelicula.iloc[0].to_dict())
        else:
            print(f"No se encontró la película con el año '{anio}'")
    return listaPeliculasA


#Clase nodo para el arbol AVL
class Node:

    def __init__(self, data: Any) -> None:
        self.data = data
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.balance: Optional[int] = 0

#Clase arbol AVL y diferentes metodos que pueden resultar utiles
class AVLTree:

    def __init__(self, root: Optional["Node"] = None) -> None:
        self.root = root

    def update_balance(self, node: Optional["Node"]) -> None:
        if node is not None:
            node.balance = self.__height_r(node.right) - self.__height_r(node.left)
            
    def preorder(self) -> None:
        self.__preorder_r(self.root)
        print()

    def __preorder_r(self, node: Optional["Node"]) -> None:
        if node is not None:
            print(node.data, end = ' ')
            self.__preorder_r(node.left)
            self.__preorder_r(node.right)

    def inorder(self) -> None:
        self.__inorder_r(self.root)
        print()

    def __inorder_r(self, node: Optional["Node"]) -> None:
        if node is not None:
            self.__inorder_r(node.left)
            print(node.data, end = ' ')
            self.__inorder_r(node.right)

    def postorder(self) -> None:
        self.__postorder_r(self.root)
        print()

    def __postorder_r(self, node: Optional["Node"]) -> None:
        if node is not None:
            self.__postorder_r(node.left)
            self.__postorder_r(node.right)
            print(node.data, end = ' ')

    def height(self) -> int:
        return self.__height_r(self.root)

    #Funcion para obtener la altura(nivel) de un nodo
    def __height_r(self, node: Optional["Node"]) -> int:
        if node is None:
            return 0
        return 1 + max(self.__height_r(node.left), self.__height_r(node.right))
    
    def num_nodes(self) -> int:
        return self.__num_nodes_r(self.root)
    
    def __num_nodes_r(self, node: Optional["Node"]) -> int:
        if node is None:
            return 0
        return 1 + self.__num_nodes_r(node.left) + self.__num_nodes_r(node.right)
    
    
    def Rot_simple_left(self, node: Optional["Node"]) -> Optional["Node"]:
        aux = node.right
        node.right = aux.left
        aux.left = node
        return aux
    
    def Rot_simple_right(self, node: Optional["Node"]) -> Optional["Node"]:
        aux = node.left
        node.left = aux.right
        aux.right = node
        return aux
    
    def Rot_double_left(self, node: Optional["Node"]) -> Optional["Node"]:
        node.right = self.Rot_simple_right(node.right)
        return self.Rot_simple_left(node)
    
    def Rot_double_right(self, node: Optional["Node"]) -> Optional["Node"]:
        node.left = self.Rot_simple_left(node.left)
        return self.Rot_simple_right(node)
    
    def insert(self, data: dict) -> None:
        self.root = self.__insert_r(self.root, data)

    def __insert_r(self, node: Optional["Node"], data: dict) -> Optional["Node"]:
        if node is None:
            return Node(data)
        if data['Title'] < node.data['Title']:
            node.left = self.__insert_r(node.left, data)
        else:
            node.right = self.__insert_r(node.right, data)
        self.update_balance(node)
        if node.balance == -2:
            if data['Title'] < node.left.data['Title']:
                return self.Rot_simple_right(node)
            else:
                return self.Rot_double_right(node)
        if node.balance == 2:
            if data['Title'] > node.right.data['Title']:
                return self.Rot_simple_left(node)
            else:
                return self.Rot_double_left(node)
        return node
    
    def eliminar(self, data: dict) -> None:
        self.root = self.__eliminar_r(self.root, data)
        
    def __eliminar_r(self, node: Optional["Node"], data: dict) -> Optional["Node"]:
        if node is None:
            return None
        if data['Title'] < node.data['Title']:
            node.left = self.__eliminar_r(node.left, data)
        elif data['Title'] > node.data['Title']:
            node.right = self.__eliminar_r(node.right, data)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            aux = self.__min_r(node.right)
            node.data = aux.data
            node.right = self.__eliminar_r(node.right, aux.data)
        self.update_balance(node)
        if node.balance == -2:
            if self.__height_r(node.left.left) >= self.__height_r(node.left.right):
                return self.Rot_simple_right(node)
            else:
                return self.Rot_double_right(node)
        if node.balance == 2:
            if self.__height_r(node.right.right) >= self.__height_r(node.right.left):
                return self.Rot_simple_left(node)
            else:
                return self.Rot_double_left(node)
        return node
    
    def buscar(self, data: dict) -> bool:
        return self.__buscar_r(self.root, data)
    
    def __buscar_r(self, node: Optional["Node"], data: dict) -> bool:
        if node is None:
            return False
        if data['Title'] < node.data['Title']:
            return self.__buscar_r(node.left, data)
        elif data['Title'] > node.data['Title']:
            return self.__buscar_r(node.right, data)
        return True
    def search_with_criteria(self, year: int, min_foreign_earnings: float) -> list:
        result = []
        self.__search_with_criteria_r(self.root, year, min_foreign_earnings, result)
        return result

    def __search_with_criteria_r(self, node: Optional["Node"], year: int, min_foreign_earnings: float, result: list) -> None:
      if node is not None:
          # Filtrar por los criterios: Año, domestic_percent < foreign_percent, y foreign_earnings >= min_foreign_earnings
          if (node.data['Year'] == year and
              node.data['Domestic Percent Earnings'] < node.data['Foreign Percent Earnings'] and
              node.data['Foreign Earnings'] >= min_foreign_earnings):
              result.append(node)

          self.__search_with_criteria_r(node.left, year, min_foreign_earnings, result)
          self.__search_with_criteria_r(node.right, year, min_foreign_earnings, result)


    def get_level(self, data: Any) -> int:
        return self.__get_level_r(self.root, data, 0)

    def __get_level_r(self, node: Optional["Node"], data: Any, level: int) -> int:
        if node is None:
            return -1  # Si no se encuentra el nodo
        if node.data == data:
            return level
        downlevel = self.__get_level_r(node.left, data, level + 1)
        if downlevel != -1:
            return downlevel
        return self.__get_level_r(node.right, data, level + 1)


    def get_balance_factor(self, node: "Node") -> int:
        return node.balance if node else 0


    def find_parent(self, data: Any) -> Optional["Node"]:
        return self.__find_parent_r(self.root, None, data)

    def __find_parent_r(self, node: Optional["Node"], parent: Optional["Node"], data: Any) -> Optional["Node"]:
        if node is None:
            return None
        if node.data == data:
            return parent
        if data < node.data:
            return self.__find_parent_r(node.left, node, data)
        else:
            return self.__find_parent_r(node.right, node, data)


    def find_grandparent(self, data: Any) -> Optional["Node"]:
        parent = self.find_parent(data)
        if parent:
            return self.find_parent(parent.data)
        return None


    def find_uncle(self, data: Any) -> Optional["Node"]:
        parent = self.find_parent(data)
        grandparent = self.find_grandparent(data)
        if grandparent is None:
            return None
        if grandparent.left == parent:
            return grandparent.right
        else:
            return grandparent.left


    def level_order(self) -> None:
        h = self.height()
        for i in range(1, h + 1):
            self.__print_given_level(self.root, i)
        print()

    def __print_given_level(self, node: Optional["Node"], level: int) -> None:
        if node is None:
            return
        if level == 1:
            print(node.data['Title'], end=" ")
        elif level > 1:
            self.__print_given_level(node.left, level - 1)
            self.__print_given_level(node.right, level - 1)


def menu():
    print("1. Insertar peliculas al arbol")
    print("2. Eliminar peliculas del arbol")
    print("3. Buscar peliculas en el arbol")
    print("4. Buscar peliculas por criterios")
    print("5. Recorrido por niveles")
    print("6. Información adicional de un nodo")
    print("7. Salir")
    op=int(input("Ingrese la opcion deseada: "))
    while op<1 or op>7:
        op=int(input("Ingrese la opcion deseada: "))
        
    return op

def general(arbol): 
    op=menu()
    if op==1:
        op1, numPeliculas=menu_inicial()
        if op1==1:
            lista=cargar_nombre(numPeliculas, data)
        elif op1==2:
            lista=cargar_indice(numPeliculas, data)
        elif op1==3:
            lista=cargar_anio(numPeliculas, data)
        arbol = crear_arbol(lista)
        graficar_arbol(arbol)
        general(arbol)
    elif op==2:
        nombre=input("Ingrese el nombre de la pelicula que desea eliminar del arbol: ")
        pelicula = data[data['Title'].str.upper() == nombre.upper()]
        arbol.eliminar(pelicula.iloc[0].to_dict())
        graficar_arbol(arbol)
        general(arbol)
    elif op==3:
        nombre=input("Ingrese el nombre de la pelicula que desea buscar en el arbol: ")
        pelicula = data[data['Title'].str.upper() == nombre.upper()]
        print(arbol.buscar(pelicula.iloc[0].to_dict()))
        general(arbol)
    elif op==4:
        year = int(input("Ingrese el año de estreno: "))
        min_foreign_earnings = float(input("Ingrese el ingreso internacional mínimo: "))
        resultados = arbol.search_with_criteria(year, min_foreign_earnings)
        if resultados:
            print("Películas encontradas:")
            for nodo in resultados:
                print(nodo.data['Title'])
        else:
            print("No se encontraron películas que cumplan los criterios.")
    elif op==5:
        print("Recorrido por niveles:")
        arbol.level_order()
    elif op==6:
        titulo = input("Ingrese el título de la película para realizar operaciones adicionales: ")
        nodo = arbol.search(titulo)
        if nodo:
            nivel = arbol.get_level(titulo)
            balance = arbol.get_balance_factor(nodo)
            padre = arbol.find_parent(titulo)
            abuelo = arbol.find_grandparent(titulo)
            tio = arbol.find_uncle(titulo)

            print(f"Nivel del nodo: {nivel}")
            print(f"Factor de balanceo: {balance}")
            print(f"Padre: {padre.data if padre else 'No tiene padre'}")
            print(f"Abuelo: {abuelo.data if abuelo else 'No tiene abuelo'}")
            print(f"Tío: {tio.data if tio else 'No tiene tío'}")
        else:
            print(f"Película '{titulo}' no encontrada.")
    elif op==7:
        print("Ha salido del programa")
        
arbol = AVLTree()    
general(arbol)
