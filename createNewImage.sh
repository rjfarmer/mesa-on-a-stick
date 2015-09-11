#!/bin/bash

#Creates a new live image, must run as root

livecd-creator --verbose --config=ks/fedora-live-workstation.ks --fslabel=MESA --cache=/var/cache/live
