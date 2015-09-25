#!/bin/bash

export VERSION=${1:-20150908}
export FILE=mesasdk-x86_64-linux-$VERSION.tar.gz

if [[ ! -f "mesa-$VERSION.zip" ]];then
   wget --user-agent="Firefox" http://www.astro.wisc.edu/~townsend/resource/download/mesasdk/$FILE -O "mesasdk.tar.gz"
fi