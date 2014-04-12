#!/bin/bash

MONTHYESTERDAY=$(date --date "yesterday" +%B)
YEAR_yesterday=$(date --date "yesterday" +%Y)

BASEDIR=$HOME/Documents/faircam/images/2013/

CURRENTMONTH=${PWD##*/}
filenameToWorkOn="12:00.jpg"

COMPLETEPATH=$BASEDIR/$CURRENTMONTH

for f in $(ls -1 ".")
do
	if [[ -d ${f} ]]
	then
		if [[ -f "${f}/11:30.jpg" ]]
		then
			echo "${f}/11:30.jpg exists!"
			cp "${f}/11:30.jpg" "${f}-11:30.jpg"
		fi
		if [[ -f "${f}/${filenameToWorkOn}" ]]
		then
			echo "${f}/${filenameToWorkOn} exists!"
			cp "${f}/${filenameToWorkOn}" "${f}-${filenameToWorkOn}"
		fi
		if [[ -f "${f}/12:30.jpg" ]]
		then
			echo "${f}/12:30.jpg exists!"
			cp "${f}/12:30.jpg" "${f}-12:30.jpg"
		fi
	fi
done

convert -size 640x480 xc:white -background white \( -font Exo-Medium.ttf -pointsize 72 -fill "#425ea0" -gravity center -draw "text 0,0 'FAIRprogress'" \) \( -font OpenSans-Regular.ttf -pointsize 40 -fill black -gravity center -draw "text 0,200 '$MONTHYESTERDAY $YEAR_yesterday' " \) 00-00:00.jpg

convert -coalesce -layers OptimizeFrame -compress lzw $COMPLETEPATH/*.jpg $COMPLETEPATH/output.gif

convert $COMPLETEPATH/output.gif  \( -clone 0 -set delay 100 \) -swap 0,-1 +delete $COMPLETEPATH/output.gif
