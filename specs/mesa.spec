Name:           mesa
Version:        %{in_version}
Release:        1%{?dist}
Summary:        MESA

License:        GPL2 or later
URL:            http://mesa.sourceforge.net/
Source0:        mesa-r%{in_version}.zip
Source1:        mesasdk.tar.gz

BuildRequires:  binutils make perl libX11 libX11-devel zlib zlib-devel bzip2
Requires:       perl

%description
MESA


%prep
%setup -q


%build
export MESASDK_ROOT=%{buildsubdir}/mesasdk
source $MESASDK_ROOT/bin/mesasdk_init.sh
cd mesa-r%{version}
./mk

%install
rm -rf $RPM_BUILD_ROOT
cp -rp %{buildsubdir} $RPM_BUILD_ROOT/opt/mesa


%files
$RPM_BUILD_ROOT/opt/mesa/*

%doc



%changelog
* Mon Sep 14 2015 Robert Farmer
- Setup
