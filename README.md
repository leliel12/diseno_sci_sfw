# Curso doctoral FAMAF: Diseño de software para cómputo científico

[![https://github.com/leliel12/diseno_sci_sfw](https://img.shields.io/badge/DiSoftCompCi-FAMAF-ffda00)](https://github.com/leliel12/diseno_sci_sfw)

- Presentación de la materia: [slides.pdf](slides.pdf)

La ediciones anteriores pueden encontrarse en: ⏰

- [2021](https://github.com/leliel12/diseno_sci_sfw/tree/2021) (con videos)
- [2020](https://github.com/leliel12/diseno_sci_sfw/tree/2020)
- [2019](https://github.com/leliel12/diseno_sci_sfw/tree/2019)

## Clases 🏫

 **20220816** Clase 1:
  - [Analisis 1: From FATS to feets](unidad1/01_from_FATS_to_feets.ipynb).
  - [Introducción a la ingeniería de software y gestión de proyectos](unidad1/00_ing_softy.ipynb).


 **20220823** Clase 2:
  - [Alto y bajo nivel](unidad2/00_alto_nivel.ipynb).
  - [Python](unidad2/01_python.ipynb).


**20220830** Clase 3:
  - [POO](unidad2/03_OOP.ipynb)
  - [Modelo de objetos de Python](unidad2/04_model.ipynb)


**20220906** Clase 4:
  - [Stack científico de Python](unidad2/02_scipy.ipynb).
  - [Decoradores](unidad2/05_decoradores.ipynb)
  - [Exceptions](unidad2/06_exceptions.ipynb)

**20220813** Clase 5:

- [Metaprogamación](unidad2/07_meta.ipynb)
- [Taxonomía](unidad1/03_taxonomia.ipynb)

**20220827** Clase 6:

- [OOP in real world](unidad2/08_oo_real_world.ipynb)
- [Pattern matching](unidad2/09_match_statement.ipynb)
- [Intro a QA](unidad3/00_intro_qa.ipynb)


## El práctico ☢️

### Entrega 0: 04 de Octubre 2022

- **Establecer el problema científico a resolver.** Las bases teóricas del problema deben estar bien entendidas. Recordar que esto no es un proyecto de investigación científica, es un proyecto de desarrollo de software. El problema no debe tener una implementación de Python. BUSCAR en PyPI https://pypi.org/
- **Repositorio público en GitHub/Gitlab/BitBucket**. El prototipo debe estar disponible en un repositorio de github con el nombre del proyecto. Configurar el repositorio para que todos los integrantes del grupo tengan acceso.
- **Grupos:** Entre 3 y 5 personas. No hace falta que todos sean expertos en el tema. Ya tuvimos matemáticos haciendo dinámica y formación galáctica; y un biotecnólogo haciendo economía. Agarren un tema que les interese. Grupos más chicos tienen que justificarlo MUY bien. Más grandes no van a ser aceptados bajo ninguna circunstancia.


### Entrega 1: 11 de Octubre 2022

- **Prototipo funcional de código.** El prototipo debe ser capaz de resolver el problema científico propuesto. Considerar que en esta etapa no se pide ningún criterio de calidad de software, solo la funcionalidad del prototipo. El prototipo debe estar escrito en Python 3.10 válido.

### Entrega $i-ésima$:

Todas las clases van a haber consultas.

### Entrega Final (En proceso)

#### O como sacar un 10
- La funcionalidad del proyecto de software tiene que estar completa.
- El valor del Coverage `>= 90%` (ideal `~95%`).
- Todo el código tiene que tener estilo y tiene que ser validado por un linter (Ejemplos: [Flake8](https://flake8.pycqa.org) para Python, [Fortran-Linter](https://pypi.org/project/fortran-linter/) para Fortran.
  - Para la gente que use Flake8 instalar los plugins
   [`flake8-black`](https://pypi.org/project/flake8-black/) (si usan [black](https://pypi.org/project/black/)),
   [`flake8-import-order`](https://pypi.org/project/flake8-import-order/),
   [`pep8-naming`](https://pypi.org/project/pep8-naming/) y
   [`flake8-builtins`](https://pypi.org/project/flake8-builtins/)

- Usar un integrador de testing (como [tox](https://pypi.org/project/tox/) o un Make), que integre tests, coverage, check-manifest, docstyle y doc-build.
- Algún integrador continuo (travis, github actions, gitlab, circle-ci, azure, etc) que se encargue de comprobar las métricas de testing del proyecto
- Documentación online que incluya:
    - Motivación.
    - Contactos.
    - Guía de instalación.
    - Tutorial con un ejemplo práctico.
    - Referencia de API.
- README, con motivación, badges, mini guia de instalacion e información de contacto.
- LICENCIA (archivo en la raiz del repo `LICENSE` o `COPIYING`).
- Todo el proyecto versionado en github/gitlab.
- Subir el proyecto a PyPI

- Presentar informe hasta 48hs antes. Hay un [template latex sugerido](https://github.com/leliel12/diseno_sci_sfw/blob/80857c790e406017b68722be893bc180e314dca8/final/final.zip) en el repositorio Github del curso (diseno_sci_sfw). Debe incluir el contexto científico, definir el problema a resolver, explicar la API, ejemplo de uso y calidad de software.
- En el template para el informe final hay un archivo txt que contiene una lista de publicaciones listas para citar.
- El final es una presentación grupal (con slides) con tiempo máximo de 40 min, en el cual uno explica el proyecto si entrar tanto en detalles técnicos, sino mas bien USO y por que es un aporte.

### Validar el curso en otra facultad/universidad:

Si van a van a validar el curso en otro programa doctoral que no sea del de FaMAF-UNC, van a necesitar:

- [Programa de la materia](https://drive.google.com/file/d/1ZUGPy444Us3miI0BaLQgJqblri6xiMaD/view)
- CV de los profesores: Mas adelante lo agrego

## Editores 📝

Estos son los [editores o IDE](https://realpython.com/lessons/ides-vs-code-editors/) más populares en Python

- [Vim/NeoVim con *fisa-vim-config*](https://vim.fisadev.com/).
- [Emacs con Python mode](https://www.emacswiki.org/emacs/PythonProgrammingInEmacs).
- [Sublime Text](https://www.sublimetext.com/).
- [Atom](https://atom.io/).
- [VisualStudio Code](https://code.visualstudio.com/) (hay que instalar extensiones para cada lenguaje).
- [PyCharm](https://www.jetbrains.com/pycharm/) (IDE).
- [Geany](https://www.geany.org/).
- [Spyder](https://www.spyder-ide.org/) (IDE).

## Bibliografía 📚

- [Dive into Python 3](http://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf) (PDF)
- [How to Think Like a Computer Scientist: Learning with Python 3](https://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3.pdf) (PDF)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [Curso de Python para ciencias e ingenierías](https://github.com/mgaitan/curso-python-cientifico)
- [Pro-Git](https://git-scm.com/book/es/v2)
