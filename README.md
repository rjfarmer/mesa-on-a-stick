# mesa-on-a-stick

This is a fedora remix, with packages from fedora 22 https://getfedora.org/ and is in no way
affliated with the fedora project. 

It contains a pre-installed version of MESA,

http://mesa.sourceforge.net/

This based on MESA r7624 with SDK 20150908.

## Where to get it

The image comes as a 1.3G .iso file available here:

https://www.dropbox.com/s/7wfg1jg0y0u7r2j/MESA-7624.1.iso?dl=0

sha256 515096642f1ac356de13d73971817877ed175f70b95651c0cb64b5593558ab6d

md5 bc1c8b354ca7cd16259ec27e59fd2bda

## Installation instructions

Either follow the guide here:
https://fedoraproject.org/wiki/How_to_create_and_use_Live_USB
replacing "Fedora image" with the MESA.iso or read on:

### Windows
To be written


### Linux
1) Insert USB stick

2) Type
````bash
dmesg | tail 
````
and look at the end for a message similiar to
````bash
[32656.573467] sd 8:0:0:0: [sdX] Attached SCSI removable disk
````
Where sdX is sdb,sdc etc. Keep a note of this and where i type sdX insert your sd name

4) Reformat the stick to ext3 (Usually possible by right clicking the icon for the USB drive and selecting format)

3) Type
````bash
     sudo dd if=/path/to/MESA.iso of=/dev/sdX  bs=1M
````
Make sure to get the right sdX !

4) Reboot machine

5) You'll need to change the boot order usally, this means during boot press F12 or esc and select the USB device.


### Mac users
1) insert usb stick

2) open disk utility. erase the usb stick, choosing the “OS X Extended (Journaled)" format.

3) convert the .iso to a .img

````bash
   hdiutil convert -format UDRW -o /path/to/MESA.img /path/to/MESA.iso
````

   change the resulting “MESA.img.dmg” ending to “MESA.img”

4)  To find the device node of the usb stick, e.g., /dev/disk1
````bash
diskutil list
````

5) Unmount the usb drive
````bash
diskutil unmountDisk /dev/diskN
````

6) This is the dangerous command, make sure you have the diskN correct or you can really mess up your machine
````bash
  sudo dd if=/path/to/MESA.img of=/dev/rdiskN bs=1m
````
   if you see the error dd: Invalid number '1m', you are using gnu dd.
   use the same command but replace bs=1m with bs=1M

7) wait about 10 min for dd to finish

8) Type
````bash
diskutil eject /dev/diskN
````

9) restart your mac, or take the usb stick to any other mac and restart,
    while holding down the option key to bring up the "Startup Manager".

10) choose the “windows” device to boot from

11) mesa-on-stick should appear.

### Alternatively

Or alternatively you could install a virtual machine software and run the iso directly without burning it to a USB
stick.

Possible options:

qemu (Linux) http://wiki.qemu.org/Main_Page

virtualbox (Windows,Mac,Linux) https://www.virtualbox.org/wiki/Downloads


## Runtime Instructions

Things are a little different to a normal MESA run. There is no need
to ever call ./mk or ./clean (in fact you can't, I deleted the
makefiles). MESA has already been pre-compiled and exists as an
executable installed in a system wide location. This means there is
NO support for custom run_stars_extras, if you want to customize
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
folder, which is a useful place to start new projects. You should
not need to make any changes in the test_suite inlists for it to 
work, other than your own customizations.

Then edit the inlists to describe the model you want and then type:

./rn

to start the MESA run. PGSTAR is enabled by default for all runs, 
though you may want to customize the pgstar inlist.
There is also, 

./re photo_name 

to restart from a photo. 

In each folder is a sub-folder star-defaults (and binaries have both 
star-defaults and binary-defaults) which show the default inlist 
values, for parameters you do not set yourself. Editing these files 
has no effect on the MESA run.

Binary stars can be handled the same way as single stars except replace

mesa-star-cwd with mesa-binary-cwd 

and

mesa-star-test with mesa-binary-test

## Limitations
No gyre or adipls support

The data files (eos,kap etc) are limited to the default set, so they
can not be changed.

No support for making movies

No run_stars_extra

## Additional items
Nothing you do will be saved to the usb stick, so if you want to keep the results either plug in another usb stick or email them to yourself

When running you will have full sudo rights if you need to configure things

To install additional programs 
````bash
sudo dnf search program
````
to search for it, and:
````bash
sudo dnf install program_name
````
to install. Python programs general ship as python-package\_name or python3-package\_name

Ipython3, numpy,scipy and matplotlib are allready installed

## Old versions

https://www.dropbox.com/s/cxsdww393w20p0q/MESA.iso?dl=0

sha256 6e3610eed9dd86ac8acbd0a31b1d4b0dd07079e118047e08b8d9b4ba166356fe

md5 cfb6920b5988e71cf86848a27395dee8





