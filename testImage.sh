#!/bin/bash

#https://fedoraproject.org/wiki/How_to_create_and_use_a_Live_CD

FILE=${1:-"MESA.iso"}

qemu-kvm -m 2048 -vga qxl -cdrom $FILE
