#!/bin/bash
export MESA_DIR=/usr/share/mesa/
export MESA_CACHE_DIR=/usr/share/mesa/data/

mkdir -p $HOME/.cache/mesa/rates_cache
export rates_cache_dir=$HOME/.cache/mesa/rates_cache

export PGPLOT_DIR=/usr/lib64/mesa/pgplot
export OMP_NUM_THREADS=$(nproc)
