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
rm -rf *.tar.gz *.tar.bz2 *.rb */final_* data/*/cache/* */make/*.o *.pdf *.tex *.png

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/mesa
cp -rp  %{_builddir}/mesasdk $RPM_BUILD_ROOT/opt/mesa/mesasdk
cp -rp  %{_builddir}/mesa-r7624 $RPM_BUILD_ROOT/opt/mesa/mesa-r7624



%files
$RPM_BUILD_ROOT/opt/mesa/*

%doc



%changelog
* Mon Sep 14 2015 Robert Farmer
- Setup
