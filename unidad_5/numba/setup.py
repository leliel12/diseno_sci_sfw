from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup

from mult_src import cc

setup(
    name="numba_examples",
    ext_modules=[cc.distutils_extension()]
)