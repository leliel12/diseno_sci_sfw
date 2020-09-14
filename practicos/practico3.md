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
- *silence* y convierte las Exceptiones generadas en función decorada
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


#### 1. Metaclase

Dada la descripción en un diccionario (dc) de una clase *C*, implementar una
funcion `crear_clase`, que reciba dc y creee C.

- *dc* debe tener una llave *name* con el nombre de C.
- *dc* debe tener una llave *properties* la cual es una lista de diccionarios,
  y cada diccionario solo tiene dos llaves:

  1. "name": el nombre de la propiedad.
  2. "readonly": Booleano si es True, no deberia poder reescribirse luego
     de la inicializacion.
- Todas las propiedades definidas en *properties* deben inicializarse en
  el contructor.



- `{"name": 'NombreClase', "properties": [´{


