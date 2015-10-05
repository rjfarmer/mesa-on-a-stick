%define debug_package %{nil}

Name:           mesa
Version:        %{in_version}
Release:        1%{?dist}
Summary:        1-D stellar evolution code

License:        GPLv2+ and non-commercial 
URL:            http://mesa.sourceforge.net/
Source0:        mesasdk.tar.gz
Source1:        extras.zip
Source2:        mesa-r%{in_version}.zip

#We dont want any cache files in the data directory
Patch0:         0001-Turn-off-cache-files.patch


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
%setup -T -b 1 -n extras
%setup -T -b 2 -n mesa-r%{in_version}

%patch0 -p1

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
rm -rf mk src make clean LOGS photos 2>/dev/null


for r in rn re
do 
   if [[ $(head -n 1 $r) != '#!/bin/bash' ]]
   then 
      echo '#!/bin/bash' | cat - "$r" > tmp && mv tmp "$r"
   fi
         sed -i 's/\.\/star\.exe/mesa\-star/g' "$r"
         sed -i 's/star\.exe/mesa\-star/g' "$r"
         sed -i 's/\.\/star/mesa\-star/g' "$r" 
done


mv star ../.

cd $MESA_DIR
cd binary/work
./mk
rm -rf mk src make clean LOGS photos 2>/dev/null

for r in rn re
do 
   if [[ $(head -n 1 $r) != '#!/bin/bash' ]]
   then 
      echo '#!/bin/bash' | cat - "$r" > tmp && mv tmp "$r"
   fi
         sed -i 's/\.\/binary\.exe/mesa-binary/g' "$r"
         sed -i 's/binary\.exe/mesa-binary/g' "$r"
         sed -i 's/\.\/binary/mesa-binary/g' "$r"      
done

cp ../defaults/binary_history_columns.list .

mv binary ../.
cd $MESA_DIR

#Remove cache files and extra eos/kap tables we dont want
rm -rf data/*/cache/* 2>/dev/null
rm -rf data/eosDT_data/macdonald-* 2>/dev/null
rm -rf data/eosDT_data/mesa-no-rad-eosDT-* 2>/dev/null
rm -rf data/eosPT_data/mesa-no-rad-eosDT-* 2>/dev/null
rm -rf data/kap_data/gs98* 2>/dev/null
rm -rf data/kap_data/a09* 2>/dev/null
rm -rf data/kap_data/OP* 2>/dev/null
rm -rf data/kap_data/lowT_Freedman11* 2>/dev/null
rm -rf data/kap_data/lowT_fa05_gn93* 2>/dev/null
rm -rf data/kap_data/lowT_fa05a09p* 2>/dev/null
rm -rf data/kap_data/lowT_af94_gn93* 2>/dev/null

cd $MESA_DIR

# De-test-suite-ify the test suite
cd star/test_suite
rm -rf */final_* 2>/dev/null
rm -rf */*.rb 2>/dev/null
rm -rf */LOGS* */photos* */make */src */star_*  2>/dev/null
rm -rf */{ck,mk,clean} 2>/dev/null
rm -rf */docs */plotters 2>/dev/null
rm -rf */*plot_data* 2>/dev/null
rm inlist_test_suite each_* do1_* test_suite_makefile_prefix mesa_dir.rb report debugging_stuff_for_inlists clean_each_test README build_and_run 2>/dev/null


sed -i '/read_extra_star_job_inlist1/d' */inlist*
sed -i '/extra_star_job_inlist1_name/d' */inlist*

#Add inlists from star/ into the test suites, only if they need. Also remove all the ../../ from their paths

#Remove unwanted test suites
rm -rf make_massive_for_o_burn 2>/dev/null

for file in "inlist_ccsn_edep_defaults" "inlist_ccsn_explosion_defaults" "inlist_ccsn_RTI_defaults" "inlist_massive_defaults" 
do 
   for dir in */
   do 
      for i in $dir/inlist*
      do
         grep -q $file $dir/inlist* && sed -i "s/\.\.\/\.\.\/$file/$file/g" $i && cp $MESA_DIR/star/$file $dir/$file
      done
   done
done

#Fix she-bangs on rn scripts
for dir in */
do 
   for r in $dir/rn $dir/rn* $dir/re
   do 
      if [[ -e "$r" ]] 
      then
         if [[ $(head -n 1 $r) != '#!/bin/bash' ]]
         then 
            echo '#!/bin/bash' | cat - "$r" > tmp && mv tmp "$r"
         fi
         sed -i 's/\.\/star\.exe/mesa\-star/g' "$r"
         sed -i 's/star\.exe/mesa\-star/g' "$r"
         sed -i 's/\.\/star/mesa\-star/g' "$r"  
      fi
   done
#enable pgstar plots for all
   if [[ -e  $dir/inlist ]]
   then
      sed -i 's/\!pgstar_flag/pgstar_flag/g' $dir/inlist* 2>/dev/null
   fi
#As we remove extra data files, remove any references to them in the inlists
   sed -i '/\_prefix/d' $dir/inlist* 2>/dev/null
   sed -i '/\_suffix/d' $dir/inlist* 2>/dev/null
   
done


cd $MESA_DIR

cd binary/test_suite
rm -rf */final_* 2>/dev/null
rm -rf */*.rb 2>/dev/null
rm -rf */LOGS{1,2} */make */src */star_* */photos* 2>/dev/null
rm -rf */{ck,mk,clean} 2>/dev/null
rm -rf */docs */plotters 2>/dev/null
rm -rf */*plot_data* 2>/dev/null
rm -rf clean_each_binary_test do1_binary_test_source each_binary_test_run report 2>/dev/null

sed -i '/mesa_dir/d' */inlist*

#enable pgstar plots for all
for dir in */
do
   if [[ -e  $dir/inlist ]]
   then
      sed -i 's/\!pgstar_flag/pgstar_flag/g' $dir/inlist* 2>/dev/null
   fi
#As we remove extra data files, remove any references to them in the inlists
   sed -i '/_prefix/d' $dir/inlist* 2>/dev/null
   sed -i '/_suffix/d' $dir/inlist* 2>/dev/null

#Copy in binary_history
   cp ../defaults/binary_history_columns.list $dir/.
   
#Fix she-bangs on rn scripts
   for r in $dir/rn $dir/rn* $dir/re
      do 
      if [[ -e "$r" ]] 
      then
         if [[ $(head -n 1 $r) != '#!/bin/bash' ]]
         then 
            echo '#!/bin/bash' | cat - "$r" > tmp && mv tmp "$r"
         fi
         sed -i 's/\.\/binary\.exe/mesa-binary/g' "$r"
         sed -i 's/binary\.exe/mesa-binary/g' "$r"
         sed -i 's/\.\/binary/mesa-binary/g' "$r"     
      fi
   done
done


cd $MESA_DIR


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datarootdir}/mesa
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{_libdir}/mesa
mkdir -p %{buildroot}%{_libexecdir}/mesa

#Compiled exectuables
cp -v star/star %{buildroot}%{_libexecdir}/mesa/star
cp -v binary/binary %{buildroot}%{_libexecdir}/mesa/binary

#Data directory without cache files in
cp -vr data %{buildroot}%{_datarootdir}/mesa/



#Default files
cp -rv star/defaults %{buildroot}%{_datarootdir}/mesa/star-defaults
cp -rv binary/defaults %{buildroot}%{_datarootdir}/mesa/binary-defaults

#Default work directories
cp -rv star/work %{buildroot}%{_datarootdir}/mesa/star-work
cp -rv binary/work %{buildroot}%{_datarootdir}/mesa/binary-work
#Copy in default history and profile column files
cp -rv star/defaults/history_columns.list %{buildroot}%{_datarootdir}/mesa/star-work/.
cp -rv star/defaults/profile_columns.list %{buildroot}%{_datarootdir}/mesa/star-work/.

cp -rv star/defaults/history_columns.list %{buildroot}%{_datarootdir}/mesa/binary-work/.
cp -rv star/defaults/profile_columns.list %{buildroot}%{_datarootdir}/mesa/binary-work/.
cp -rv binary/defaults/binary_history_columns.list %{buildroot}%{_datarootdir}/mesa/binary-work/.

#Copy the defaults folders
cp -rv star/defaults %{buildroot}%{_datarootdir}/mesa/star-work/star-defaults
cp -rv  star/defaults %{buildroot}%{_datarootdir}/mesa/binary-work/star-defaults
cp -rv  binary/defaults %{buildroot}%{_datarootdir}/mesa/binary-work/binary-defaults


#Grab the test suite
cp -rv star/test_suite %{buildroot}%{_datarootdir}/mesa/star-test-suite
cp -rv binary/test_suite %{buildroot}%{_datarootdir}/mesa/binary-test-suite

pushd $(pwd)

cd %{buildroot}%{_datarootdir}/mesa/star-test-suite
for i in */
do
   cd $i
   ln -sf %{_datarootdir}/mesa/star-defaults star-defaults
   cd ../
done

cd ../../

cd %{buildroot}%{_datarootdir}/mesa/binary-test-suite
for i in */
do
   cd $i
   ln -sf %{_datarootdir}/mesa/star-defaults star-defaults
   ln -sf %{_datarootdir}/mesa/binary-defaults binary-defaults
   cd ../
done

popd

#Adds script to /etc/profile.d which adds the enviroment varaibles we need
cp ../extras/mesa-custom.sh %{buildroot}%{_sysconfdir}/profile.d/mesa-custom.sh

#extra shell scripts used
cp ../extras/mesa-star* %{buildroot}%{_bindir}/.
cp ../extras/mesa-binary* %{buildroot}%{_bindir}/.
cp ../extras/INSTRUCTIONS.txt %{buildroot}%{_datarootdir}/mesa/.

#Customized images_to_movie.sh
#cp ../extras/images_to_movie.sh %{buildroot}%{_bindir}/.

#Adds needed libraries from the sdk
cp -rv ../mesasdk/lib64/*.so* %{buildroot}%{_libdir}/mesa/
cp -rv ../mesasdk/lib/*.so* %{buildroot}%{_libdir}/mesa/
cp -rv --remove-destination ../mesasdk/pgplot %{buildroot}%{_libdir}/mesa/pgplot

#Fix pgplot link
cd %{buildroot}%{_libdir}/mesa/
ln -sf pgplot/libpgplot.so libpgplot.so 
cd -

#Remove rpaths
chrpath --delete %{buildroot}%{_libexecdir}/mesa/star
chrpath --delete %{buildroot}%{_libexecdir}/mesa/binary


#########SDK
#cp ../mesasdk/bin/ff* %{buildroot}%{_bindir}/.
cp ../mesasdk/bin/h5* %{buildroot}%{_bindir}/.
#cp ../mesasdk/bin/x264 %{buildroot}%{_bindir}/.






%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files 
%attr(0755, root, root) %{_bindir}/*
%attr(0755, root, root) %{_libexecdir}/mesa/*
%{_datarootdir}/mesa/*-work/inlist*
%{_datarootdir}/mesa/*-work/*.list
%{_datarootdir}/mesa/*-work/*-defaults
%{_datarootdir}/mesa/*-work/README
%{_datarootdir}/mesa/INSTRUCTIONS.txt
%attr(0755, root, root) %{_datarootdir}/mesa/*-work/rn*
%attr(0755, root, root) %{_datarootdir}/mesa/*-work/re

%{_datarootdir}/mesa/star-defaults
%{_datarootdir}/mesa/binary-defaults
%attr(0644, root, root) %{_sysconfdir}/profile.d/mesa-custom.sh
%{_libdir}/mesa/*

%files data
%{_datarootdir}/mesa/data/*

%files examples
%attr(0644, root, root) %{_datarootdir}/mesa/star-test-suite/*/inlist*
%attr(0644, root, root) %{_datarootdir}/mesa/binary-test-suite/*/inlist*
%attr(0644, root, root) %{_datarootdir}/mesa/star-test-suite/*/*.list
%attr(0644, root, root) %{_datarootdir}/mesa/binary-test-suite/*/*.list
%{_datarootdir}/mesa/star-test-suite/*/star-defaults
%{_datarootdir}/mesa/binary-test-suite/*/star-defaults
%{_datarootdir}/mesa/binary-test-suite/*/binary-defaults
%attr(0644, root, root) %{_datarootdir}/mesa/star-test-suite/*/*.mod
%attr(0644, root, root) %{_datarootdir}/mesa/*-test-suite/*/*.in
%attr(0644, root, root) %{_datarootdir}/mesa/star-test-suite/*/readme*
%attr(0644, root, root) %{_datarootdir}/mesa/star-test-suite/*/README*
%attr(0644, root, root) %{_datarootdir}/mesa/star-test-suite/*/HOW_TO
%attr(0644, root, root) %{_datarootdir}/mesa/star-test-suite/8.8M_urca/urca.*
%attr(0644, root, root) %{_datarootdir}/mesa/star-test-suite/wd_aic/aic.*
%attr(0644, root, root) %{_datarootdir}/mesa/star-test-suite/wd_o_ne_ignite/wd_o_ne_ignite.net
%attr(0644, root, root) %{_datarootdir}/mesa/star-test-suite/make_low_mass_with_uniform_composition/list
%attr(0644, root, root) %{_datarootdir}/mesa/star-test-suite/create_zahb/zahb_masses.list_big
%attr(0644, root, root) %{_datarootdir}/mesa/star-test-suite/irradiated_planet/irrad_out.txt
%attr(0644, root, root) %{_datarootdir}/mesa/star-test-suite/solar_calibration/ttt.adipls.prt
%attr(0644, root, root) %{_datarootdir}/mesa/star-test-suite/wd_aic/wd_aic.net


%attr(0644, root, root) %{_datarootdir}/mesa/binary-test-suite/jdot_gr_check/.restart


%attr(0755, root, root) %{_datarootdir}/mesa/*-test-suite/*/rn*
%attr(0755, root, root) %{_datarootdir}/mesa/*-test-suite/*/re
%attr(0755, root, root) %{_datarootdir}/mesa/star-test-suite/make_planets/runscript.py*

%doc



%changelog
* Mon Sep 14 2015 Robert Farmer <rjfarmer@asu.edu> - 1.0.0
- Setup
