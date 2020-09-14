# Diseño de software para cómputo científico
## Unidad 1 - Práctico II - Clases

**Fecha de resolución:** 17/09/2020

### Criterios

- Se debe escribir todos los programas para Python 3.8
- Al finalizar del modulo debe haber un main que ejecuta todos los ejercicios.
- El archivo no debe tirar errores de estilo [PEP 8](https://www.python.org/dev/peps/pep-0008/) (Verificarlo con la
  herramienta *Flake8* y *Black*
- Implementar sin `attrs` ni `dataclass`.

#### Notas

- Flake 8: [http://flake8.pycqa.org](http://flake8.pycqa.org)
- Black: [https://github.com/psf/black](https://github.com/psf/black)


### Ejercicios

#### 1. Puerta

Un cerrojo con combinación tiene las siguientes propiedades básicas: la combinación
(una secuencia de tres números); el cerrojo se puede abrir proporcionando la combinación; y
la combinación se puede cambiar, pero solamente por alguien que conoce la combinación actual.

Diseñe una clase con métodos `abrir`, `cerrar` y `cambiar_combinacion`, y
atributos para almacenar la combinación y el estado de la puerta, cerrada o abierta.

La combinación debería asignarse en el constructor.

#### 2. Herencia

Establezca una jerarquía de clases que represente a los estudiantes de una
universidad sabiendo que todos los estudiantes se caracterizan por un nombre y un
número. Hay varios tipos de estudiantes: los estudiantes ocasionales, sean de cursos
de verano o de cursos específicos (se matriculan de un curso determinado), los que
cursan solo una tecnicatura, licenciatura.

Además, la universidad imparte cursos de especialización gratuitos para sus empleados.

#### 3. Triángulo

Escriba una clase, `Triángulo`, que represente un triángulo.

La clase debe incluir los
siguientes métodos que devuelven un valor lógico indicando el tipo del triángulo:
es_rectangulo (devuelve `True` para triángulos rectángulos)
es_escaleno (devuelve `True`  todos los lados distintos)
es_isosceles (devuelve `True` dos lados iguales y el otro distinto)
es_equilatero (devuelve `True` los tres lados iguales)

#### 4. Personas

Construya una estructura de clases que represente una serie de personas
caracterizadas por el nombre (compuesto de nombre de pila y dos apellidos) y el
número del DNI. Debe ser posible imprimir los datos completos de una persona y
devolver el nombre o el DNI independientemente.

#### 5. Vínculos

Modifique el ejemplo anterior para poder construir un árbol genealógico donde se
establezca dinámicamente un vínculo que indique qué persona es el padre y cual la
madre de una persona dada.

#### 6. Introspección

Implementar la función evaluar que tome un objeto y un string como parámetros
y si el string es un atributo, que devuelva el valor del atributo.

Si es un método, devolver el resultado de aplicar el método al objeto
(usar parámetros opcionales en evaluar para parámetros de métodos con
parámetros) y si no es un método, ni un atributo, lanzar una Exception del
tipo UnkonowTypeError que es-un TypeError el cual recibe comp parámetro
el nombre del atributo desconocido.
