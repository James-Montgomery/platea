#!/usr/bin/env bash

# chmod +x make.sh

alias f2py="python -m numpy.f2py"

./clean.sh

f2py -c --verbose --fcompiler=gfortran --opt='-O3  -ftree-vectorize -march=native -fcheck=bounds' \
  types.f90 -m types

f2py -c --verbose --fcompiler=gfortran --opt='-O3  -ftree-vectorize -march=native -fcheck=bounds' \
  types.f90 random_number_generators.f90 -m ran_num_gen

f2py -c --verbose --fcompiler=gfortran --opt='-O3  -ftree-vectorize -march=native -fcheck=bounds' \
  types.f90 special_functions.f90 -m spcl_fnc

f2py -c --verbose --fcompiler=gfortran --opt='-O3  -ftree-vectorize -march=native -fcheck=bounds' \
  types.f90 random_number_generators.f90 special_functions.f90 distributions.f90 -m dist
