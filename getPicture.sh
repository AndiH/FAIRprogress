#!/bin/bash
# Will download the current FAIR construction site picture and save it according to the current date

YEAR=$(date +%Y)
MONTH=$(date +%m)
DAY=$(date +%d)
HOUR=$(date +%H)
MINUTE=$(date +%M)

FILENAME=$HOUR:$MINUTE.jpg

PREFIX="images"
CURRENTDIR=$YEAR/$MONTH/$DAY
ABSOLUTEPATH=/var/www/vhosts/andreasherten.de/httpdocs/andreasherten/fair
COMPLETEPATH=$ABSOLUTEPATH/$PREFIX/$CURRENTDIR

TEMPPATH=$ABSOLUTEPATH/imgtmp

if ! [ -d "$COMPLETEPATH" ]
then
	mkdir -p $COMPLETEPATH
	cp "$ABSOLUTEPATH/$PREFIX/index.php" "$COMPLETEPATH"
fi


wget http://www.fair-center.eu/fileadmin/fair/webcam/webcam001/FAIRcam001.jpg -O "$TEMPPATH/$FILENAME"

MIMETYPE=$(file --mime-type -b $TEMPPATH/$FILENAME)

if [ "$MIMETYPE" = "image/jpeg" ]
then
	mv $TEMPPATH/$FILENAME $COMPLETEPATH
else
	rm $TEMPPATH/$FILENAME
fi

