#!/bin/bash

export VERSION=${1:-7624}

if [[ ! -f "mesa-$VERSION.zip" ]];then
   wget http://sourceforge.net/projects/mesa/files/releases/mesa-r"$VERSION".zip/download -O mesa.zip
fi