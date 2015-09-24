#!/bin/bash

#Builds a rpm for mesa

VERSION=${1:-7624}

BUILD_DIR="$(pwd)"

CLEAN=1

if [[ $CLEAN -eq 1 ]]
then
   rm -rf "$BUILD_DIR"/RPMBUILD
   mkdir -p "$BUILD_DIR"/RPMBUILD/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
   #ln -sf "$BUILD_DIR"/RPMBUILD $HOME/rpmbuild

   export BUILDROOT="/home/rob/mesa-on-a-stick/RPMBUILD/"

   ln -s  "$BUILD_DIR"/mesa-r$VERSION.zip "$BUILD_DIR"/RPMBUILD/SOURCES/mesa-r$VERSION.zip
   ln -s  "$BUILD_DIR"/mesasdk.tar.gz "$BUILD_DIR"/RPMBUILD/SOURCES/mesasdk.tar.gz
   
   zip "$BUILD_DIR"/patches/mesa-custom.zip "$BUILD_DIR"/patches/mesa-custom/*
   cp "$BUILD_DIR"/patches/mesa-custom.zip "$BUILD_DIR"/RPMBUILD/SOURCES/mesa-custom.zip
  
   rm -rf mesa-repo
   mkdir mesa-repo
fi

rpmbuild --define="_topdir $BUILD_DIR/RPMBUILD/" --define="in_version $VERSION" -ba specs/mesa.spec 2>&1 | tee rpm.log

rpmlint specs/mesa.spec $BUILD_DIR/RPMBUILD/SRPMS/* $BUILD_DIR/RPMBUILD/RPMS/x86_64/* | tee rpmlint.log 

if [[ $? -eq 0 && -e $BUILD_DIR/RPMBUILD/RPMS/x86_64/mesa-"$VERSION"-1.fc22.x86_64.rpm ]] 
then
   cp $BUILD_DIR/RPMBUILD/RPMS/x86_64/mesa*.rpm mesa-repo/.
   rm -rf $BUILD_DIR/RPMBUILD
   createrepo mesa-repo
fi