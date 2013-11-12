#!/bin/bash

YEAR_yesterday=$(date --date "yesterday" +%Y)
MONTH_yesterday=$(date --date "yesterday" +%m)
DAY_yesterday=$(date --date "yesterday" +%d)

YEAR_twodaysago=$(date --date "2 days ago" +%Y)
MONTH_twodaysago=$(date --date "2 days ago" +%m)
DAY_twodaysago=$(date --date "2 days ago" +%d)

BASEDIR=$HOME/Documents/faircam
PREFIX="images"
CURRENTDIR_yesterday=$YEAR_yesterday/$MONTH_yesterday/$DAY_yesterday
COMPLETEPATH=$BASEDIR/$PREFIX/$CURRENTDIR_yesterday


DELAY="20" #-delay $DELAY

#create small GIF
convert -resize 320 -coalesce -colors 16 -layers OptimizeFrame -compress lzw $COMPLETEPATH/*.jpg $COMPLETEPATH/output--small.gif
#create big GIF
convert -coalesce -layers OptimizeFrame -compress lzw $COMPLETEPATH/*.jpg $COMPLETEPATH/output.gif
#echo $CURRENTPATH/$CURRENTDIR_yesterday/output_small.gif
#echo "$CURRENTPATH/$YEAR_yesterday-$MONTH_yesterday-$DAY_yesterday--small.gif"

cp -f $COMPLETEPATH/output--small.gif "$BASEDIR/$YEAR_yesterday-$MONTH_yesterday-$DAY_yesterday--small.gif"
cp -f $COMPLETEPATH/output.gif "$BASEDIR/$YEAR_yesterday-$MONTH_yesterday-$DAY_yesterday.gif"
rm $BASEDIR/$YEAR_twodaysago-$MONTH_twodaysago-$DAY_twodaysago--small.gif
rm $BASEDIR/$YEAR_twodaysago-$MONTH_twodaysago-$DAY_twodaysago.gif

#LATESTFILE=$(ls -1 *.gif | tail -n 1)

#GETSECONDS_OSX=$(stat -f "%m" $LATESTFILE)
#CONVERTEDTIME_OSX=$(date -j -f "%s" "$GETSECONDS_OSX" +"%d.%m.%Y %R")

#GETSECONDS_UNIX=$(stat -c %Y $LATESTFILE)
#CONVERTEDTIME_UNIX=$(date -d @$GETSECONDS_UNIX +"%d.%m.%Y %R")