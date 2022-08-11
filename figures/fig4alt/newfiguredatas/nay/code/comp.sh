#!/bin/bash
rm *.mod
gfortran -O3 -o exe my_init.f95 random.f95 mcint.f95 mconf.f95 sort.f95 quartile.f95 main.f95 -mcmodel=medium
