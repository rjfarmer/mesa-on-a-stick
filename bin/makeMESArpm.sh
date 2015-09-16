#!/bin/bash

#Builds a rpm for mesa

VERSION=${1:-7624}

BUILD_DIR="$(pwd)"


rm -rf "$BUILD_DIR"/RPMBUILD
mkdir -p "$BUILD_DIR"/RPMBUILD/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
ln -sf "$BUILD_DIR"/RPMBUILD $HOME/rpmbuild

export BUILDROOT="/home/rob/mesa-on-a-stick/RPMBUILD/"

ln -s  "$BUILD_DIR"/mesa-r$VERSION.zip "$BUILD_DIR"/RPMBUILD/SOURCES/mesa-r$VERSION.zip
ln -s  "$BUILD_DIR"/mesasdk.tar.gz "$BUILD_DIR"/RPMBUILD/SOURCES/mesasdk.tar.gz


rpmbuild --buildroot="$BUILD_DIR"/RPMBUILD --define="in_version $VERSION" -ba specs/mesa.spec