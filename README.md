# mesa-on-a-stick

This is a fedora remix, with packages from fedora 22 https://getfedora.org/ and is in no way
affliated with the fedora project. 

It contains a pre-installed version of MESA http://mesa.sourceforge.net/

## Where to get it

The image comes as a 1.3G .iso file available here:
https://www.dropbox.com/s/cxsdww393w20p0q/MESA.iso?dl=0

sha256 6e3610eed9dd86ac8acbd0a31b1d4b0dd07079e118047e08b8d9b4ba166356fe
md5 cfb6920b5988e71cf86848a27395dee8

## Installation instructions

Follow the guide here:
https://fedoraproject.org/wiki/How_to_create_and_use_Live_USB
replacing "Fedora image" with the MESA.iso

Or alternatively you could install a virtual machine software
(like qemu) and run the iso directly without burning it to a USB
stick.

## Instructions

Things are a little different to a normal MESA run. There is no need
to ever call ./mk or ./clean (in fact you can't, I deleted the
maakefiles). MESA has already been pre-compiled and exists as an
executable installed in a system wide location. This means there is
*NO* support for custom run_stars_extras, if you want to customize
your run_stars_extra file then you will need to use the normal 
installation methods.

To run MESA in this new scheme:

1) Open a terminal by double clicking it

2) Either type

mesa-star-cwd folder_name

or

mesa-star-test test_suite_name folder_name

Where folder_name is the name to save the folder to and
test_suite_name is a name of a MESA test suite folder (in the second case 
you can tap TAB TAB to get a list of possible folders). The
difference between the commands is the mesa-star-cwd creates a copy
of the default work directory, which is a basic shell of what you
need to run a model. While mesa-star-test copies a MESA test suite
folder,  hich is a useful place to start new projects. You should
not need to make any changes in the test_suite inlists for it to 
work, other than your own  customization's.

Then edit the inlists to describe the model you want and then type:

./rn

to start the MESA run. PGSTAR is enabled by default for all runs, 
though you may want to customize the pgstar inlist.
There is also ./re photo_name to restart from a photo. 

In the folder is a sub-folder star-defaults (and binaries have both 
star_defaults and binary-ddefaults) which show the default inlists 
values for parameters you do not set yourself. Editing these files 
will have no effect on the MESA run.

Binary stars can be handled the same way as single stars except replace

mesa-star-cwd with mesa-binary-cwd and

mesa-star-test with mesa-binary-test

## Limitations
No gyre or adipls support

The data files (eos,kap etc) are limited to the default set, so they
can not be changed.

No support for making movies
