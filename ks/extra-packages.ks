%packages --excludedocs

#Remove Fedora trademarks
-fedora-logos
-fedora-release
-fedora-release-notes

+generic-logos
+generic-release
+generic-release-notes

#MESA dependicies
+binutils
+make
+perl
+libX11
+libX11-devel
+zlib
+zlib-devel

#Other packages
+ipython
+ipython3
+numpy
+scipy
+matplotlib
+python3-numpy
+python3-scipy
+python3-matplotlib

#remove unnesacry packages
-libreoffice*
-evolution
-rhythmbox
-hunspell*

%end
