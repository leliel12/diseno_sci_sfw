
from numpy.distutils.core import setup
from numpy.distutils.core import Extension


EXTENSIONS = [
    Extension(name="vectores",
              sources=["vectores.f90"],
              extra_compile_args=[],
              extra_link_args=[])
]


setup(
    name="fortran_examples",
    ext_modules=EXTENSIONS)
