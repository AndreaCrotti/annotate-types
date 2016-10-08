from setuptools import setup, find_packages

from annotate_types import __version__

package = 'annotate_types'

setup(name=package,
      version=__version__,
      packages=['annotate_types'],
      description="annotate your code with voluptuous types",
      author="Andrea Crotti",
      setup_requires=["GitPython>=2.0"],
      author_email="andrea.crotti.0@gmail.com",
      license='MIT',
      classifiers=[
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy"],
      url='https://github.com/AndreaCrotti/annotate-types')
