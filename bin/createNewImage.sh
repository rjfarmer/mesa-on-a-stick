#!/bin/bash

#Creates a new live image, must run as root

rm -rf cache/live/mesa-repo

livecd-creator --verbose --config=main.ks --fslabel=MESA --cache=cache/live -t tmp/ 2>&1 | tee build.log
