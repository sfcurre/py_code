from distutils.core import setup, Extension
setup(name = 'mathspace', version = '1.0', ext_modules = [Extension('mathspace', ['mathspace.c'])])