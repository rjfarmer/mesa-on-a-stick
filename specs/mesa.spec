#No debug info
%define debug_package %{nil}
#Dont strip static archives
%define %{__strip} %{nil}

Name:           mesa
Version:        %{in_version}
Release:        1%{?dist}
Summary:        MESA

License:        GPL2 or later
URL:            http://mesa.sourceforge.net/
Source0:        mesasdk.tar.gz
Source1:        mesa-r%{in_version}.zip


BuildRequires:  binutils make perl libX11 libX11-devel zlib zlib-devel bzip2
Requires:       perl make

%description
MESA


%prep
%setup -n mesasdk
%setup -T -b 1 -n mesa-r%{in_version}


%build
export MESASDK_ROOT=%{_builddir}/mesasdk
source $MESASDK_ROOT/bin/mesasdk_init.sh
#As we extract mesa after the sdk we are allready in the mesa dir
./mk
rm -rf **/*.tar.gz **/*.tar.bz2 **/*.rb **/*/final_* */make/*.o **/*.rb **/*.png 
rm -rf data/*/cache/* **/star_history **/star_profile svnup 
rm -rf **/test

%install
rm -rf $RPM_BUILD_ROOT/opt
mkdir -p $RPM_BUILD_ROOT/opt/mesa
cp -rvp  %{_builddir}/mesasdk $RPM_BUILD_ROOT/opt/mesa/mesasdk
cp -rvp  %{_builddir}/mesa-r7624 $RPM_BUILD_ROOT/opt/mesa/mesa-r7624



%files
/opt/mesa/*

%doc



%changelog
* Mon Sep 14 2015 Robert Farmer
- Setup
