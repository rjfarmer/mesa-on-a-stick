#!/bin/bash
export MESA_DIR=/usr/share/mesa/
export MESA_CACHE_DIR=/dev/true

export eosDT_cache_dir=/dev/true
export eosPT_cache_dir=/dev/true
export eosDE_cache_dir=/dev/true
export ionization_cache_dir=/dev/true
export kap_cache_dir=/dev/true
export rates_cache_di=/dev/true

export PGPLOT_DIR=/usr/lib64/mesa/pgplot
export OMP_NUM_THREADS=$(nproc)


alias mesa-star="LD_LIBRARY_PATH=/usr/lib64/mesa /usr/bin/mesa-star"