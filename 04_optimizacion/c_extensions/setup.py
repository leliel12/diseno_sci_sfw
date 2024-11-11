from setuptools import setup, Extension

setup(
    ext_modules=[
        Extension(
            name="fputs",
            sources=["fputsmodule.c"],
        ),
    ],
)
