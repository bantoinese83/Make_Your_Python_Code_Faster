from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

extensions = [
    Extension(
        "cython_example",
        ["cython_example.pyx"],
        include_dirs=[numpy.get_include()],  # Include NumPy headers if needed
        extra_compile_args=["-O3"],  # Optimization flag
        extra_link_args=[],
    ),
    # Add more extensions here if needed
]

setup(
    name="cython_example",
    ext_modules=cythonize(
        extensions,
        compiler_directives={"language_level": "3", "boundscheck": False, "wraparound": False},
    ),
    zip_safe=False,
)
