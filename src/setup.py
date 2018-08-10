from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Compiler import Options

from config.build import bios as SBIOS


from Cython.Distutils import build_ext


ext_modules = []

for name, files in SBIOS.COMPILE_FILES:
    ext = Extension(name, files)
    ext_modules.append(ext)

Options.annotate = False
Options.emit_code_comments = True
Options.docstrings = False
Options.embed = 'main'


setup(name='bios app',
        # zip_safe=False,
        ext_modules=cythonize(ext_modules, build_dir='../build/c'))
