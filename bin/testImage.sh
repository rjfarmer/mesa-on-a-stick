#!/bin/bash

#https://fedoraproject.org/wiki/How_to_create_and_use_a_Live_CD

FILE=${1:-"MESA.iso"}

qemu-kvm -m 4096 -smp 4 -vga qxl -cdrom $FILE
