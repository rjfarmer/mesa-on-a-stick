# Maintained by the Fedora Workstation WG:
# http://fedoraproject.org/wiki/Workstation
# mailto:desktop@lists.fedoraproject.org

%post

# This is a huge file and things work ok without it
rm -f /usr/share/icons/HighContrast/icon-theme.cache

cat >> /etc/rc.d/init.d/livesys << EOF


# disable updates plugin
cat >> /usr/share/glib-2.0/schemas/org.gnome.software.gschema.override << FOE
[org.gnome.software]
download-updates=false
FOE

# don't run gnome-initial-setup
mkdir ~liveuser/.config
touch ~liveuser/.config/gnome-initial-setup-done

mkdir -p ~liveuser/Desktop
cp /usr/share/applications/firefox.desktop ~liveuser/Desktop/firefox.desktop

sed -i 's/Excec\=firefox/Exec\=firefox\ \%u\ http\:\/\/mesa\.sourceforge\.net/' ~liveuser/Desktop/firefox.desktop

cp /usr/share/applications/org.gnome.Terminal.desktop ~liveuser/Desktop/org.gnome.Terminal.desktop
cp /usr/share/mesa/INSTRUCTIONS.txt ~liveuser/Desktop/INSTRUCTIONS.txt

cat >> /usr/share/glib-2.0/schemas/org.gnome.shell.gschema.override << FOE
[org.gnome.shell]
favorite-apps=['firefox.desktop', 'org.gnome.Nautilus.desktop','org.gnome.Terminal.desktop']

[org.gnome.desktop.background]
show-desktop-icons=true

[org.gnome.shell]
enabled-extensions=['launch-new-instance@gnome-shell-extensions.gcampax.github.com','window-list@gnome-shell-extensions.gcampax.github.com','apps-menu@gnome-shell-extensions.gcampax.github.com']

[org.gnome.desktop.wm.preferences]
button-layout='appmenu:minimize,maximize,close'

[org.gnome.desktop.sound]
event-sounds=false

[org.gnome.desktop.privacy]
report-technical-problems=false
send-software-usage-stats=false

[org.gnome.desktop.datetime]
automatic-timezone=true

FOE


# rebuild schema cache with any overrides we installed
glib-compile-schemas /usr/share/glib-2.0/schemas

# set up auto-login
cat > /etc/gdm/custom.conf << FOE
[daemon]
AutomaticLoginEnable=True
AutomaticLogin=liveuser
FOE

# Turn off PackageKit-command-not-found while uninstalled
if [ -f /etc/PackageKit/CommandNotFound.conf ]; then
  sed -i -e 's/^SoftwareSourceSearch=true/SoftwareSourceSearch=false/' /etc/PackageKit/CommandNotFound.conf
fi

# make sure to set the right permissions and selinux contexts
chown -R liveuser:liveuser /home/liveuser/
restorecon -R /home/liveuser/

EOF


%end
