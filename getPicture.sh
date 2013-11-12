#!/bin/bash
# Will download the current FAIR construction site picture and save it according to the current date

YEAR=$(date +%Y)
MONTH=$(date +%m)
DAY=$(date +%d)
HOUR=$(date +%H)
MINUTE=$(date +%M)

PREFIX="images"
CURRENTDIR=$YEAR/$MONTH/$DAY
ABSOLUTEPATH=$HOME/Documents/faircam/$PREFIX/$CURRENTDIR

if ! [ -d "$ABSOLUTEPATH" ]
then
	mkdir -p $ABSOLUTEPATH
fi

wget http://www.fair-center.eu/fileadmin/fair/webcam/webcam001/FAIRcam001.jpg -O "$ABSOLUTEPATH/$HOUR:$MINUTE.jpg"