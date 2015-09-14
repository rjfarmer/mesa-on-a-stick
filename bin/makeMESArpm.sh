#!/bin/bash

#Builds a rpm for mesa

VERSION=${1:-7624}

rm -rf RPMBUILD
mkdir -p RPMBUILD/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

export BUILDROOT="/home/rob/mesa-on-a-stick/RPMBUILD/"
cp  mesa-r$VERSION.zip RPMBUILD/SOURCES/mesa-r$VERSION.zip
cp  mesasdk.tar.gz RPMBUILD/SOURCES/mesasdk.tar.gz


rpmbuild --buildroot="/home/rob/mesa-on-a-stick/RPMBUILD/" --define="in_version $VERSION" -ba specs/mesa.spec