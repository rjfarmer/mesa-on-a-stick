#No debug info
%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}
#Dont strip static archives

Name:           mesa
Version:        %{in_version}
Release:        1%{?dist}
Summary:        MESA

License:        GPLv2 or later
URL:            http://mesa.sourceforge.net/
Source0:        mesasdk.tar.gz
Source1:        mesa-custom.zip
Source2:        mesa-r%{in_version}.zip



BuildRequires:  binutils make perl libX11 libX11-devel zlib zlib-devel bzip2 zip
AutoReqProv: no

%description
MESA


%prep
%setup -n mesasdk
%setup -T -b 1 -n mesa-custom
%setup -T -b 2 -n mesa-r%{in_version}

%build
export MESASDK_ROOT=%{_builddir}/mesasdk
source $MESASDK_ROOT/bin/mesasdk_init.sh
export MESA_DIR=%{_builddir}/mesa-r%{in_version}
#As we extract mesa last we are allready in the mesa dir
cd $MESA_DIR
./mk
cd $MESA_DIR
cd star/work
./mk
rm -rf mk src make rn re clean LOGS photos 2>/dev/null
mv star ../.

cd $MESA_DIR
cd binary/work
./mk
rm -rf mk src make rn re clean LOGS photos 2>/dev/null
mv binary ../.
cd $MESA_DIR

#Remove the data files leaviing just the cache files except for the
#rates folder where we leave the data files.
rm -rf data/eosDT_data/*.data 2>/dev/null
rm data/eosDT_data/helm_table.dat 2>/dev/null
rm -rf data/eosDE_data/*.data 2>/dev/null
rm -rf data/eosPT_data/*.data 2>/dev/null
rm -rf data/ionization_data/*.data 2>/dev/null
rm -rf data/rates_data/cache/* 2>/dev/null
rm -rf data/kap_data/*.data 2>/dev/null
cd $MESA_DIR

# De-test-suite-ify the test suite
cd star/test_suite
rm -rf */final_* 2>/dev/null
rm -rf */*.rb 2>/dev/null
rm -rf */LOGS */make */src */star_* 2>/dev/null
rm -rf */{ck,mk,clean} 2>/dev/null
rm -rf */docs */plotters 2>/dev/null
rm -rf */*plot_data* 2>/dev/null
rm inlist_test_suite each_* do1_* 2>/dev/null

sed -i '/read_extra_star_job_inlist1/d' */inlist*
sed -i '/extra_star_job_inlist1_name/d' */inlist*

#Add inlists from star/ into the test suites, only if they need. Also remove all the ../../ from their paths
for file in "inlist_ccsn_edep_defaults" "inlist_ccsn_explosion_defaults" "inlist_ccsn_RTI_defaults" "inlist_massive_defaults"; do for dir in */; do grep -q $file $dir/inlist* && sed -i "s/\.\.\/\.\.\/$file/$file/g" $dir/inlist* && cp $MESA_DIR/star/$file $dir/$file;  done; done

cd $MESA_DIR

cd binary/test_suite
rm -rf */final_* 2>/dev/null
rm -rf */*.rb 2>/dev/null
rm -rf */LOGS{1,2} */make */src */star_* 2>/dev/null
rm -rf */{ck,mk,clean} 2>/dev/null
rm -rf */docs */plotters 2>/dev/null
rm -rf */*plot_data* 2>/dev/null
rm -rf clean_each_binary_test do1_binary_test_source each_binary_test_run report 2>/dev/null

sed -i '/mesa_dir/d' */inlist*

cd $MESA_DIR

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datarootdir}/mesa

cp -vp star/star %{buildroot}%{_bindir}/mesa-star
cp -vp binary/binary %{buildroot}%{_bindir}/mesa-binary
cp -vrp data %{buildroot}%{_datarootdir}/mesa/data
cp -rvp star/defaults %{buildroot}%{_datarootdir}/mesa/star-defaults
cp -rvp binary/defaults %{buildroot}%{_datarootdir}/mesa/binary-defaults
cp -rvp star/work %{buildroot}%{_datarootdir}/mesa/star-work
cp -rvp binary/work %{buildroot}%{_datarootdir}/mesa/binary-work

cp -rvp star/test_suite %{buildroot}%{_datarootdir}/mesa/star-test-suite
cp -rvp binary/test_suite %{buildroot}%{_datarootdir}/mesa/binary-test-suite

mkdir -p %{buildroot}%{_libdir}/mesa
cp -rvp ../mesasdk/lib64/*.so* %{buildroot}%{_libdir}/mesa/
cp -rvp ../mesasdk/lib/*.so* %{buildroot}%{_libdir}/mesa/
cp -rvp --remove-destination ../mesasdk/pgplot %{buildroot}%{_libdir}/mesa/pgplot

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cp ../mesa-custom/mesa-custom.sh %{buildroot}%{_sysconfdir}/profile.d/mesa-custom.sh



%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files 
%defattr(-,root,root,-)
%{_bindir}/mesa-star
%{_bindir}/mesa-binary
%{_datarootdir}/mesa/*
%{_libdir}/mesa/*
%{_sysconfdir}/profile.d/mesa-custom.sh

%doc



%changelog
* Mon Sep 14 2015 Robert Farmer
- Setup
