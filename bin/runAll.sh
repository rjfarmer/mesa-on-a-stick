#!/bin/bash

#Note this isnt fully automated yet but gives the ordering of scripts

echo "Dont run just look"
exit 0

bin/livecd-dependices.sh
bin/getMESA.sh
bin/getSDK.sh
bin/makeMESArpm.sh
bin/createNewImage.sh
bin/testImage.sh
