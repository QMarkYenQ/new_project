

from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension



sourcefiles = ['mycodecpy.pyx', 'mycode.c']

extensions = [Extension("mycodecpy", sourcefiles)]

setup(
    ext_modules = cythonize(extensions)
)