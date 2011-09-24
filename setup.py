from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("quvi", ["src/quvi.pyx"], libraries=['quvi'])]

setup(
  name = 'Quvi',
  author = 'Patrice FERLET',
  author_email = "metal3d@gmail.com",
  url="https://github.com/metal3d/python-quvi",
  description="libquvi wrapper module",
  license="LGPLv2.1+",
  version="0.0.1-beta",
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)