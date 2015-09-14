#Remove timeout on grub

%packages

grub2-tools

%end


%post

sed -i 's/GRUB\_TIMEOUT\=.*/GRUB\_TIMEOUT\=0/' /etc/default/grub

grub2-mkconfig -o /boot/grub2/grub.cfg

%end