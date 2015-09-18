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
AutoReqProv: no

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
find . -name *.tar.gz -delete 2>/dev/null
find . -name *.tar.bz2 -delete 2>/dev/null
find . -name *.tar.zip -delete 2>/dev/null
rm -rf star/test_suite/*/final_*  2>/dev/null
find . -name *.o -delete 2>/dev/null
find . -name *.rb -delete 2>/dev/null
find */make -name *.mod -delete 2>/dev/null
rm -rf eos/data/* 2>/dev/null 
find star -name star_history/*  -delete 2>/dev/null
find star -name star_profile/* -delete 2>/dev/null
find star -name plotters/* -delete 2>/dev/null
find star -name plot_data/* -type d -delete 2>/dev/null
rm -f svnup clean mk install 2>/dev/null
find */test/* -delete 2>/dev/null

#Remove the data files leaviing just the cache filesm except for the
# rates folder which we leave the data files.
rm -rf data/eosDT_data/*.data 2>/dev/null
rm data/eosDT_data/helm_table.dat
rm -rf data/eosDE_data/*.data 2>/dev/null
rm -rf data/eosPT_data/*.data 2>/dev/null
rm -rf data/ionization_data/*.data 2>/dev/null
rm -rf data/rates_data/cache/* 2>/dev/null
rm -rf data/kap_data/*.data 2>/dev/null
rm -rf */preprocessor
rm -rf eos/eos*_builder 2>/dev/null
rm -rf website xeon_phi_sample 2>/dev/null
rm data/rates_data/jina_reaclib_results05301331

%install
rm -rf $RPM_BUILD_ROOT/opt
mkdir -p $RPM_BUILD_ROOT/opt/mesa
cp -rvp  %{_builddir}/mesasdk $RPM_BUILD_ROOT/opt/mesa/mesasdk
cp -rvp  %{_builddir}/mesa-r7624 $RPM_BUILD_ROOT/opt/mesa/mesa-r7624



%files  
%defattr(-,liveuser,liveuser,-)
/opt/mesa/*

%doc



%changelog
* Mon Sep 14 2015 Robert Farmer
- Setup
