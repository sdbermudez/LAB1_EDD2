# Proyecto de Estructura de Datos: Árbol AVL de Películas

Este proyecto implementa un sistema de gestión de películas utilizando un árbol AVL (Árbol Balanceado de Altura). Se utiliza un archivo CSV (`dataset_movies.csv`) que contiene una lista de películas con información relevante, como el título y el año. El objetivo principal es permitir la inserción, eliminación, búsqueda y otras operaciones en el árbol AVL, optimizando el equilibrio del árbol después de cada operación.

## Dependencias

Este proyecto utiliza las siguientes bibliotecas:
- `os`: Para manejar rutas de archivos.
- `pandas`: Para la manipulación y lectura de archivos CSV.
- `networkx` y `matplotlib`: Para la visualización gráfica del árbol AVL.

Instalación de dependencias:
```bash
pip install pandas networkx matplotlib


##Funcionalidades
Menú Inicial
El programa presenta un menú interactivo donde el usuario puede elegir entre varias opciones:
1. Cargar películas al árbol (por nombre, índice o año).
2. Eliminar películas del árbol.
3. Buscar películas en el árbol.
4. Buscar películas con criterios específicos.
5. Realizar un recorrido por niveles del árbol.
6. Obtener información adicional de un nodo.
7. Salir del programa.

Estructura del Árbol AVL
El árbol AVL está implementado en la clase AVLTree, que contiene métodos para insertar, eliminar, y buscar nodos, además de realizar rotaciones simples y dobles para mantener el equilibrio del árbol.

##Operaciones Disponibles
1. Insertar Películas: Inserta un número específico de películas en el árbol, ya sea por nombre, índice o año.
2. Eliminar Películas: Elimina una película del árbol según su título.
3. Buscar Películas: Verifica si una película específica está en el árbol.
4. Buscar con Criterios: Busca películas que cumplan con criterios como el año de estreno y un ingreso mínimo en taquilla internacional.
5. Recorrido por Niveles: Muestra las películas en el árbol utilizando un recorrido por niveles.
6. Información de Nodo: Muestra detalles adicionales sobre un nodo, incluyendo su nivel, factor de balance, padre, abuelo y tío en el árbol.
7. Visualización del Árbol
El programa incluye una función graficar_arbol que utiliza networkx y matplotlib para visualizar gráficamente la estructura del árbol AVL.

Ejecución
Para ejecutar el programa, simplemente ejecuta el archivo Python:

```bash
python lab1_EDD_Final.py

El programa cargará el dataset de películas y te permitirá interactuar con el árbol AVL a través del menú en la consola.
