%packages --excludedocs

#Remove Fedora trademarks
#-fedora-logos
#-fedora-release
#-fedora-release-notes
#-fedora-release-21-2

#generic-logos
#generic-release
#generic-release-notes

#MESA dependicies
binutils
make
perl
libX11
libX11-devel
zlib
zlib-devel

#Other packages
python3-ipython
python3-numpy
python3-scipy
python3-matplotlib

#remove unnesacry packages
-openoffice*
-evolution
-rhythmbox
-hunspell*
-@printing
-hunspell
-iscsi*
-sane*
-abrt*
-qemu*
-mdadm*
-git*
-libvert*
-@fonts
-@dial-up
-@multimedia
-@printing
-@libreoffice
%end
