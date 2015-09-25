%define debug_package %{nil}

Name:           mesa
Version:        %{in_version}
Release:        1%{?dist}
Summary:        1-D stellar evolution code

License:        GPLv2+ and non-commercial 
URL:            http://mesa.sourceforge.net/
Source0:        mesasdk.tar.gz
Source1:        mesa-custom.zip
Source2:        mesa-r%{in_version}.zip



BuildRequires:  binutils make perl libX11 libX11-devel zlib zlib-devel bzip2 zip chrpath
Requires:    mesa-data mesa-examples
AutoReqProv: no

%description
MESA (Modules for Expirments in Stellar Astrophysics) is a 1-D
stellar evolution code.

%package data
Summary:       Data files needed for mesa
AutoReqProv: no

%description data
MESA data

%package examples
Summary:       Test suite examples for mesa
AutoReqProv: no

%description examples
MESA examples

%prep
#http://www.rpm.org/max-rpm/s1-rpm-inside-macros.html
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
rm -rf */LOGS* */photos* */make */src */star_*  2>/dev/null
rm -rf */{ck,mk,clean} 2>/dev/null
rm -rf */docs */plotters 2>/dev/null
rm -rf */*plot_data* 2>/dev/null
rm inlist_test_suite each_* do1_* 2>/dev/null


sed -i '/read_extra_star_job_inlist1/d' */inlist*
sed -i '/extra_star_job_inlist1_name/d' */inlist*

#Add inlists from star/ into the test suites, only if they need. Also remove all the ../../ from their paths
for file in "inlist_ccsn_edep_defaults" "inlist_ccsn_explosion_defaults" "inlist_ccsn_RTI_defaults" "inlist_massive_defaults" 
do 
   for dir in */
   do 
      grep -q "$file" "$dir/inlist*" && sed -i "s/\.\.\/\.\.\/$file/$file/g" "$dir/inlist*" && cp "$MESA_DIR/star/$file" "$dir/$file"
   done
done

#Fix she-bangs on rn scripts
for dir in */
do 
   for r in "$dir/rn*"
   do 
      if [[ $(head -n 1 $r) != '#!/bin/bash' ]]
      then 
         echo '#!/bin/bash' | cat - "$r" > tmp && mv tmp "$r"
      fi
   done
done



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
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{_libdir}/mesa
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d

#Compiled exectuables
cp -v star/star %{buildroot}%{_bindir}/mesa-star
cp -v binary/binary %{buildroot}%{_bindir}/mesa-binary

#Data direcotry with cache files in
cp -vr data %{buildroot}%{_datarootdir}/mesa/data

#Default files
cp -rv star/defaults %{buildroot}%{_datarootdir}/mesa/star-defaults
cp -rv binary/defaults %{buildroot}%{_datarootdir}/mesa/binary-defaults

#Default wokr directories
cp -rv star/work %{buildroot}%{_datarootdir}/mesa/star-work
cp -rv binary/work %{buildroot}%{_datarootdir}/mesa/binary-work

#Grab the test suite
cp -rv star/test_suite %{buildroot}%{_datarootdir}/mesa/star-test-suite
cp -rv binary/test_suite %{buildroot}%{_datarootdir}/mesa/binary-test-suite

#Adds script to /etc/profile.d which adds the enviroment varaibles we need
cp ../mesa-custom/mesa-custom.sh %{buildroot}%{_sysconfdir}/profile.d/mesa-custom.sh

#Adds needed libraries from the sdk
cp -rv ../mesasdk/lib64/*.so* %{buildroot}%{_libdir}/mesa/
cp -rv ../mesasdk/lib/*.so* %{buildroot}%{_libdir}/mesa/
cp -rv --remove-destination ../mesasdk/pgplot %{buildroot}%{_libdir}/mesa/pgplot

#Fix pgplot link
cd %{buildroot}%{_libdir}/mesa/
ln -sf pgplot/libpgplot.so libpgplot.so 
cd -

#Make ld.so.conf.d/file
cat > %{buildroot}%{_sysconfdir}/ld.so.conf.d/mesa-star-x86_64.conf << EOF
%{_libdir}/mesa/
%{_libdir}/mesa/pgplot
EOF
#Remove rpaths
chrpath --delete %{buildroot}%{_bindir}/mesa-star
chrpath --delete %{buildroot}%{_bindir}/mesa-binary



%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files 
%defattr(-,root,root,-)
%{_bindir}/mesa-star
%{_bindir}/mesa-binary
%{_datarootdir}/mesa/star-work
%{_datarootdir}/mesa/binary-work
%{_datarootdir}/mesa/star-defaults
%{_datarootdir}/mesa/binary-defaults
%{_sysconfdir}/profile.d/mesa-custom.sh
%{_sysconfdir}/ld.so.conf.d/mesa-star-x86_64.conf
%{_libdir}/mesa/*

%files data
%defattr(-,root,root,-)
%{_datarootdir}/mesa/data/*

%files examples
%defattr(-,root,root,-)
%{_datarootdir}/mesa/star-test-suite/*
%{_datarootdir}/mesa/binary-test-suite/*


%doc



%changelog
* Mon Sep 14 2015 Robert Farmer
- Setup
