#Packages

%packages --excludedocs

#Stuff to remove
-@dial-up
-@input-methods
-@standard
-@fonts
-@libreoffice
-gfs2-utils
-reiserfs-utils
-mpage
-sox
-hplip
-hpijs
-numactl
-isdn4k-utils
-autofs
-coolkey
-xsane
-xsane-gimp
-sane-backends
-anaconda*
-libvirt*
-qemu*
-devassistant*
-libreoffice*
-rhythmbox*
-shotwell
-evolution*
-abrt*
-cheese
-gnome-boxes*
-transmission-gtk


# Explicitly specified here:
# <notting> walters: because otherwise dependency loops cause yum issues.
kernel

# This was added a while ago, I think it falls into the category of
# "Diagnosis/recovery tool useful from a Live OS image".  Leaving this untouched
# for now.
memtest86+

# Need aajohan-comfortaa-fonts for the SVG rnotes images
aajohan-comfortaa-fonts


#Base set
@base-x
@core
@hardware-support
@networkmanager-submodules


#workstation-product
ModemManager
NetworkManager-adsl
NetworkManager-openconnect
NetworkManager-openvpn-gnome
NetworkManager-pptp-gnome
NetworkManager-vpnc-gnome
acl
adwaita-qt4
at
at-spi2-atk
at-spi2-core
attr
avahi
baobab
bash-completion
bc
bijiben
bind-utils
bridge-utils
btrfs-progs
bzip2
caribou
caribou-gtk2-module
caribou-gtk3-module
cheese
chrony
cifs-utils
control-center
cpio
crontabs
cryptsetup
cyrus-sasl-plain
dbus
dconf
deltarpm
dnf
dnf-plugins-core
dos2unix
dosfstools
empathy
eog
ethtool
evince
evince-browser-plugin
evince-nautilus
file
file-roller
file-roller-nautilus
firefox
fpaste
fprintd-pam
fros-gnome
gdm
gedit
glib-networking
gnome-backgrounds
gnome-bluetooth
gnome-boxes
gnome-calculator
gnome-classic-session
gnome-clocks
gnome-color-manager
gnome-contacts
gnome-disk-utility
gnome-documents
gnome-font-viewer
gnome-getting-started-docs
gnome-initial-setup
gnome-maps
gnome-screenshot
gnome-session-wayland-session
gnome-session-xsession
gnome-settings-daemon
gnome-shell
gnome-shell-extension-background-logo
gnome-software
gnome-system-monitor
gnome-terminal
gnome-themes-standard
gnome-user-docs
gnome-user-share
gnome-weather
gnupg2
google-android-emoji-fonts
gucharmap
gvfs-afc
gvfs-afp
gvfs-archive
gvfs-fuse
gvfs-goa
gvfs-gphoto2
gvfs-mtp
gvfs-smb
hunspell
ibus-chewing
ibus-gtk2
ibus-gtk3
ibus-hangul
ibus-kkc
ibus-libpinyin
ibus-m17n
ibus-qt
ibus-rawcode
ibus-typing-booster
iptstate
jwhois
libcanberra-gtk2
libcanberra-gtk3
libproxy-mozjs
librsvg2
libsane-hpaio
lrzsz
lsof
mailcap
man-pages
mcelog
microcode_ctl
mlocate
mousetweaks
mtr
nautilus
nautilus-sendto
net-tools
nfs-utils
nm-connection-editor
nmap-ncat
nss-mdns
ntfs-3g
ntfsprogs
orca
pam_krb5
pam_pkcs11
passwdqc
pciutils
pcmciautils
pinentry-gtk
pinfo
plymouth
polkit-js-engine
ppp
psacct
qt
qt-settings
qt-x11
qt5-qtbase
qt5-qtbase-gui
qt5-qtdeclarative
qt5-qtxmlpatterns
quota
rdist
realmd
rng-tools
rp-pppoe
rsync
rygel
scl-utils
seahorse
setuptool
shotwell
sos
sssd
stunnel
sudo
sushi
symlinks
tar
tcp_wrappers
tcpdump
telnet
time
totem
totem-nautilus
traceroute
tree
unoconv
unzip
usbutils
vconfig
vinagre
wget
which
wireless-tools
words
wvdial
xdg-user-dirs-gtk
xorg-x11-drv-libinput
yelp
zip

#Remove trademarked packages and replace with generic versions
#Some point may want to customize the generic packages
-fedora-logos
-fedora-release
-fedora-release-notes

generic-logos
generic-release
generic-release-notes


#MESA dependicies
mesa-data
mesa-examples
mesa-7624


#Other packages
python3-ipython
python3-numpy
python3-scipy
python3-matplotlib
nano

%end