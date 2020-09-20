# Diseño de software para cómputo científico
## Unidad 1 - Práctico II - Clases

**Fecha de resolución:** 17/09/2020

### Criterios

- Se debe escribir todos los programas para Python 3.8.
- Al finalizar del modulo debe haber un main que ejecuta todos los ejercicios.
- El archivo no debe tirar errores de estilo [PEP 8](https://www.python.org/dev/peps/pep-0008/) (Verificarlo con la
  herramienta *Flake8* y *Black*
- Implementar sin `attrs` ni `dataclass`.

#### Notas

- Flake 8: [http://flake8.pycqa.org](http://flake8.pycqa.org)
- Black: [https://github.com/psf/black](https://github.com/psf/black)


### Ejercicios

#### 1. Excepciones, warnings y decoradores

- Desarrollar un decorador `silence` que recibe N clases de Exceptions (E) como
parámetros posicionales.
- *silence* y convierte las excepciones generadas en función decorada
  que sean de los tipos E, en un `SilencedWarning` que es-un `UserWarning`.
- *SilencedWarning* tiene como mensaje la exception original como string.


En código:

```pycon
>>> @silence(ZeroDivisionError)
... def division(a, b):
...     return a / b

>>> division(1, 0)
<ipython-input-17-3775d029a994>:11: SilencedWarning: division by zero
  warnings.warn(str(err), SilencedWarning)

>>> division(1, "hola")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-21-8be8b097f3de> in <module>
----> 1 division(1, "hola")

<ipython-input-17-3775d029a994> in wrap(*args, **kwargs)
      7         def wrap(*args, **kwargs):
      8             try:
----> 9                 return func(*args, **kwargs)
     10             except E as err:
     11                 warnings.warn(str(err), SilencedWarning)

<ipython-input-20-b4289e43549f> in division(a, b)
      1 @silence(ZeroDivisionError)
      2 def division(a, b):
----> 3     return a / b
      4
      5 division(1, 0)

TypeError: unsupported operand type(s) for /: 'int' and 'str'

>>> @silence(ZeroDivisionError, TypeError)
... def division(a, b):
...    return a / b

>>> division(1, "hola")
<ipython-input-17-3775d029a994>:11: SilencedWarning: unsupported operand type(s) for /: 'int' and 'str'
  warnings.warn(str(err), SilencedWarning)
```


#### 2. TUPS - Tuple Processor

Asumamos un lenguaje de programación muy parecido a [LISP](https://es.wikipedia.org/wiki/Lisp),
en el cual el lenguaje esta representado de la forma `(O L R)` donde 

- `O` es el operador/función.
- `L` es el parámetro izquierdo, que puede ser un número u otra estructura anidada `(O L R)`.
- `R` es el parámetro derecho, que puede ser un número u otra estructura anidada `(O L R)`.

En este caso lo implementaremos con tuplas. Así la operación `(1 + 3) * 4` podría representarse como:

```python
("*", ("+", 1, 3), 4)
```

Por cuestiones de simplicidad, las funciones/operadores son representadas como string y `L` y `R`
son siempre floats o ints.


Desarrollar una función `tups()` que reciba como parámetro una epresión de este lenguaje y la resuelva. También
de soportar resolver una expresión de un solo dígito (`tups(42)` devuelve *42*). Por simplicidad solo implementar
la suma y la multiplicación.

Probar con las siguientes 3 expresiones

```python
tups(1) # debería dar 1
tups( ("+", 1, 3) )   # debería dar 4
tups( ("*", ("+", 1, 3), 4) ) # debería dar 16
tups( ("+", ("*", 37, ("+", ("*", ("+", 1, 3), 4), ("*", 4, 25))), 135) ))  # 4427
```
