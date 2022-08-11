from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup

from Cython.Build import cythonize


setup(
    name="cython_examples",
    ext_modules=cythonize(["helloworld.pyx", "primes.pyx", "primes_np.pyx", "hello_cwrapper.pyx"])
)

