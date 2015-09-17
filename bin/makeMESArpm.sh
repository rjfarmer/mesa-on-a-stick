#!/bin/bash

#Builds a rpm for mesa

VERSION=${1:-7624}

BUILD_DIR="$(pwd)"

CLEAN=1

if [[ $CLEAN -eq 1 ]]
then
   rm -rf "$BUILD_DIR"/RPMBUILD
   mkdir -p "$BUILD_DIR"/RPMBUILD/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
   ln -sf "$BUILD_DIR"/RPMBUILD $HOME/rpmbuild

   export BUILDROOT="/home/rob/mesa-on-a-stick/RPMBUILD/"

   ln -s  "$BUILD_DIR"/mesa-r$VERSION.zip "$BUILD_DIR"/RPMBUILD/SOURCES/mesa-r$VERSION.zip
   ln -s  "$BUILD_DIR"/mesasdk.tar.gz "$BUILD_DIR"/RPMBUILD/SOURCES/mesasdk.tar.gz
fi

rpmbuild --define="in_version $VERSION" -ba specs/mesa.spec