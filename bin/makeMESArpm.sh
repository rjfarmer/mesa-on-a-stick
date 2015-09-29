#!/bin/bash

#Builds a rpm for mesa

VERSION=${1:-7624}

BUILD_DIR="$(pwd)"

CLEAN=1

if [[ $CLEAN -eq 1 ]]
then
   rm -rf "$BUILD_DIR"/RPMBUILD
   mkdir -p "$BUILD_DIR"/RPMBUILD/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

   cp  "$BUILD_DIR"/mesa-r$VERSION.zip "$BUILD_DIR"/RPMBUILD/SOURCES/mesa-r$VERSION.zip
   cp  "$BUILD_DIR"/mesasdk.tar.gz "$BUILD_DIR"/RPMBUILD/SOURCES/mesasdk.tar.gz
   
   cd patches
   zip "$BUILD_DIR"/patches/extras.zip extras/*
   cp "$BUILD_DIR"/patches/extras.zip "$BUILD_DIR"/RPMBUILD/SOURCES/extras.zip
   
   cp *.patch "$BUILD_DIR"/RPMBUILD/SOURCES/.
   
   cd -
  
   rm -rf mesa-repo
   mkdir mesa-repo
fi

rpmbuild --define="_topdir $BUILD_DIR/RPMBUILD" --define="in_version $VERSION" -ba specs/mesa.spec 2>&1 | tee rpm.log

rpmlint specs/mesa.spec $BUILD_DIR/RPMBUILD/SRPMS/* $BUILD_DIR/RPMBUILD/RPMS/x86_64/* | tee rpmlint.log 

if [[ $? -eq 0 && -e $BUILD_DIR/RPMBUILD/RPMS/x86_64/mesa-"$VERSION"-1.fc22.x86_64.rpm ]] 
then
   cp $BUILD_DIR/RPMBUILD/RPMS/x86_64/mesa*.rpm mesa-repo/.
   rm -rf $BUILD_DIR/RPMBUILD
   createrepo mesa-repo
fi