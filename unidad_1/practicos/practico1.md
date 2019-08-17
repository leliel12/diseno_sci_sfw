# Diseño de software para cómputo científico
## Unidad 1 - Practico I

### Criterio de evaluación

- Se debe escribir todos los programas para Python 3.7
- Se recomienda crear un entorno virtual para aislar los scripts del problema.
- Cada ejercicio debe ser una función, cuya documentación debe ser su enunciado
- Al finalizar del modulo debe haber un main que ejecuta todos los ejercicios.
- El cumplimento de estos criterios es parte de la evaluación.
- El archivo debe llamarse `u1e1_apellido.py`
- El archivo no debe tirar errores de estilo [PEP 8](https://www.python.org/dev/peps/pep-0008/) (Verificarlo con la
  herramienta *Flake8*

#### Notas

- Flake 8: [http://flake8.pycqa.org](http://flake8.pycqa.org)
- Entornos virtuales en Python 3: [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)
- Como crear entornos virtuales con anaconda:  [https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- Como crear entornos virtuales con virtualenv [https://virtualenv.pypa.io](https://virtualenv.pypa.io)


### Ejercicios 

#### 1. Strings

##### 1.1 Facturas

Dado una número de facturas, implementar una función que devuleva el string `Cantidad de facturas: <nro>` donde `nro` es el número que se pasa como argumento. Si las facturas son mas de 12, se tiene que devolver `Cantidad de facturas: muchas`.

1.2 Ambos
Dado un string s, implementar la función ambos que devuelve un string construido con los dos primeros y dos últimos caracteres. Por ejemplo, aplicar ambos a  ‘primavera’ devuelve ‘prra’. Si  s posee menos de dos caracteres, el resultado es el string vacio.

1.3. Fix
Dado un string s, implementar una función fix que reemplaza todas las ocurrencias del primer caracter por ‘*’ a excepción de la primera ocurrencia. Por ejemplo evaluar fix a la palabra ‘burbuja’ devuelve ‘bur*uja’. 
Ayuda, estudiar la función replace.

1.4. Mezclar
Dados dos strings a y b, implementar la función mezclar que devuleve el string a y b separados por un espacio, excepto las primeros caracteres de cada string que son intercambiados. Por ejemplo, mezclar(‘mix’, ‘pod’) devuelve ‘pix mod’.

2. Listas

2.1. Macheos
Implementar la función macheos que dada una lista de strings devuelve un número representando la cantidad de strings que tienen mas de dos caracteres y cuyos últimos dos strings son iguales.
Nota: python no posee operador ++ pero += funciona.

2.2. front_x
Dada una lista de strings, implementar la funcion front_x que devuelve una lista ordenada exceptuando las palabras que comiencen con x, las cuales deben ir al principio. Por ejemplo, ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] devuelve ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']

2.3. sort_last
Dada una lista de tuplas no vacias, implementar la funcion sort_last que devuelve una lista con las tuplas ordenadas de forma incremental en el último elemento de la tupla. Ejemplo: aplicar sort_last a [(1, 7), (1, 3), (3, 4, 5), (2, 2)] devuelve [(2, 2), (1, 3), (3, 4, 5), (1, 7)]

2.4. Tablas de multiplicar
Implementar la función tablas que dado un argumento nro, devuelve la tabla de multiplicar de nro del 1 al 10.

3. Diccionarios

3.1. Mapeo
Implementar la función mapeo que toma un string y devuelve un diccionario con cada caracter como clave y la posición del caracter como valor. Ejemplo, evaluar mapeo a ‘casa’ devuelve {‘c’: 0, ‘a’:1, ‘s’:2,}

3.2. Busqueda reversa
Implementar la función busqueda_reversa que dado un diccionario y un objeto cualquiera, permita buscar por valores de diccionarios en vez de claves. Ejemplo: 
>>> d = {‘c’: 0, ‘a’:1, ‘s’:2, ‘a’: 3}
>>> busqueda_reversa(d, 3)
’a’

4. Ejercicios difíciles

4.1. Invitados
Imaginen que poseemos un diccionario de la forma nombre -> estado (clave -> valor), el estado representa si la persona cuyo nombre es nombre irá o no a tu cumpleaños, por ejemplo:

>>> invitados = {"María": "Asistirá", "Luis": "Asistirá", "Ángel": "No asistirá",
... "Pedro": "Asistirá", "Carla": "No asistirá"}

Implementar la función invitados que devuelve solo aquellas personas que asistirán al cumpleaños.

4.2. Dado un string implementar la función justificar que fija la longitud de cada línea en 80 caracteres y justifica cada línea. 
