#Packages

%packages --excludedocs

#Stuff to remove
-@dial-up
-@input-methods
-@standard
-@fonts
-@printing
-@libreoffice
-gfs2-utils
-reiserfs-utils
-mpage
-sox
-hplip
-hpijs
-numactl
-isdn4k-utils
-autofs
-coolkey
-xsane
-xsane-gimp
-sane-backends
-anaconda*
-libvirt*
-qemu*
-devassistant*
-libreoffice*
-rhythmbox*
-shotwell
-evolution*
-abrt*
-cheese
-totem*
-gnome-boxes*
-transmission-gtk


# Explicitly specified here:
# <notting> walters: because otherwise dependency loops cause yum issues.
kernel

# This was added a while ago, I think it falls into the category of
# "Diagnosis/recovery tool useful from a Live OS image".  Leaving this untouched
# for now.
memtest86+

# Need aajohan-comfortaa-fonts for the SVG rnotes images
aajohan-comfortaa-fonts


#Base set
@base-x
@core
@hardware-support
@networkmanager-submodules
@workstation-product --nodefaults


#MESA dependicies
mesa-data
mesa-examples
mesa-7624


#Other packages
python3-ipython
python3-numpy
python3-scipy
python3-matplotlib
nano

%end