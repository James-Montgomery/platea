#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" setup script to install platea """

import os
import setuptools
from numpy.distutils.core import setup, Extension

# python3 -m pip install --user --upgrade setuptools wheel
# rm -rf build && rm -rf dist && rm -rf *.info
# python3 setup.py sdist bdist_wheel
# python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

################################################################################

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

with open("README.md", "r") as fh:
    """ load package description from readme file """
    long_description = fh.read()

################################################################################

fortran_path = "./platea/_fortran/"
types_path = fortran_path + "types.f90"
rng_path = fortran_path + "random_number_generators.f90"
spcl_fnc_path = fortran_path + "special_functions.f90"
dist_path = fortran_path + "distributions.f90"

compiler_args = ["-O3",  "-ftree-vectorize", "-march=native", "-fcheck=bounds"]

ext1 = Extension(name = "platea._fortran.types",
                 sources = [types_path],
                 extra_f90_compile_args=compiler_args,
                 extra_f77_compile_args=compiler_args,
                 extra_link_args=compiler_args)

ext2 = Extension(name = "platea._fortran.ran_num_gen",
                 sources = [types_path, rng_path],
                 extra_f90_compile_args=compiler_args,
                 extra_f77_compile_args=compiler_args,
                 extra_link_args=compiler_args)

ext3 = Extension(name = "platea._fortran.spcl_fnc",
                 sources = [types_path, spcl_fnc_path],
                 extra_f90_compile_args=compiler_args,
                 extra_f77_compile_args=compiler_args,
                 extra_link_args=compiler_args)

ext4 = Extension(name = "platea._fortran.dist",
                 sources = [types_path, rng_path, spcl_fnc_path, dist_path],
                 extra_f90_compile_args=compiler_args,
                 extra_f77_compile_args=compiler_args,
                 extra_link_args=compiler_args)

extensions = [ext1, ext2, ext3, ext4]

################################################################################
# a mess of failed trials ... sigh

# import numpy
# from numpy.distutils.command.sdist import sdist
# from numpy.distutils.command.install import install

# class build_ext(numpy.distutils.command.build_ext.build_ext):
#     def run(self):
#         self.inplace = True
#         return numpy.distutils.command.build_ext.build_ext.run(self)

# class install(numpy.distutils.command.install.install):
#     def run(self):
#         #self.run_command("build_ext")
#         build_ext().run()
#         return numpy.distutils.command.install.install.run(self)

# class build_py(numpy.distutils.command.build_py.build_py):
#     def run(self):
#         self.run_command("build_ext")
#         return super().run()

# https://stackoverflow.com/questions/19569557/pip-not-picking-up-a-custom-install-cmdclass
# https://stackoverflow.com/questions/41586547/python-3-setup-py-pip-install-that-does-everything-build-ext-install
# https://stackoverflow.com/questions/29477298/setup-py-run-build-ext-before-anything-else

# class CustomSDistCommand(sdist):
#     def run(self):
#         os.system("python setup.py build_ext --inplace")
#         sdist.run(self)
#
# class CustomInstallCommand(install):
#     def run(self):
#         os.system("python setup.py build_ext --inplace")
#         install.run(self)

################################################################################

def setup_package():
    """
    Function to manage setup procedures.
    """

    # ~/opt/anaconda3/envs/python_env/lib/python3.7/site-packages/platea/

    # check package list
    # python setup.py sdist

    setup(
        name="platea",
        version="0.0.1",
        author="James Montgomery",
        author_email="jamesoneillmontgomery@gmail.com",
        description="A package for statistics and numeric methods.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/James-Montgomery/stats",
        python_requires=">=3.6",
        latforms='any',
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        packages=setuptools.find_packages(),
        install_requires=parse_requirements("requirements.txt"),
        extra_require={},
        ext_modules = extensions,
        #cmdclass={'install' : CustomInstallCommand, 'sdist': CustomSDistCommand}
        #cmdclass={'install' : install, 'build_ext' : build_ext, 'build_py': build_py}
    )

if __name__ == "__main__":
    setup_package()
