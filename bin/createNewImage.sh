#!/bin/bash

#Creates a new live image, must run as root

livecd-creator --verbose --config=main.ks --fslabel=MESA --cache=cache/live 2>&1 | tee build.log
