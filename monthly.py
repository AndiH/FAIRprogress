#!/usr/bin/python
# -*- coding: utf-8

#
#  Generate the monthly FAIRprogress
# ------------------------------------

# import stuff
import sys, os          # system functions (like exit, file handling)
import datetime         # time functions
import calendar         # calendar stuff
import astral           # sunrise stuff
import re               # regular expressions
import tempfile         # handle temporary files/directories

_city = 'Darmstadt'
_region = 'Germany'
_latitude = "49°52'N"
_longitude = "8°39'E"
_elevation = 144
_timezone = 'Europe/Berlin'

_dataDir = './'
_frames = 100


# get all the months that don't have a monthly gif created yet
def getMonths():
    months = []
    candidateYear = 0
    candidateMonth = 0
    for dirname, dirnames, filenames in os.walk(_dataDir):
        for subdirname in dirnames:
            # top directory should contain year
            if dirname == _dataDir and re.match("^\d{4}$", subdirname) is not None:
                candidateYear = int(subdirname)

            # first subdirectory should contain the months
            if dirname == (_dataDir + "{}".format(candidateYear)):
                candidateMonth = int(subdirname)
                candidateFilename = "{:4d}-{:02d}.gif".format(candidateYear, candidateMonth)

                # TODO: check if all days are complete / month != currentMonth
                if not os.path.exists(dirname +"/"+ subdirname +"/"+ candidateFilename):
                    months.append((candidateYear, candidateMonth))
    return months


# returns the list of time stamps
def getContinuousImageSequence(startTime, stopTime, daysOfMonth):
    minutesPerDay = (stopTime - startTime)/daysOfMonth
    nextDaySwitch = startTime + minutesPerDay
    currentTime = startTime
    currentDay = 1
    imageList = []
    while currentTime < stopTime:
        currentTime += datetime.timedelta(minutes=15)
        imageList.append( "{0:02d}/{1:02d}:{2:02d}.jpg".format(currentDay, currentTime.hour, currentTime.minute) )
        if currentTime > nextDaySwitch:
            currentDay += 1
            nextDaySwitch += minutesPerDay
    return imageList


def writeGif(imageList, startTime):
    dir = tempfile.mkdtemp()
    baseDir = _dataDir + "{0}/{1:02d}/".format(startTime.year, startTime.month)

    # create the title image
    filepath = dir + "/00:00.jpg"
    os.system('convert -size 640x480 xc:white -background white \( -font Exo-Medium.ttf -pointsize 72 -fill "#425ea0" -gravity center -draw "text 0,0 \'FAIRprogress\'" \) \( -font OpenSans-Regular.ttf -pointsize 40 -fill black -gravity center -draw "text 0,200 \'{0} {1}\' " \) {2}'.format(startTime.strftime("%B"), startTime.year, filepath))

    # copy the files to include
    for file in imageList:
        filepath = baseDir + file
        os.system("cp {0} {1}".format(filepath, dir))

    # make the gif
    outFile = dir + "/{0}-{1:02d}.gif".format(startTime.year, startTime.month)
    os.system('convert -coalesce -layers OptimizeFrame -compress lzw {0}/*.jpg {1}'.format(dir, outFile))
    os.system('convert {0}  \( -clone 0 -set delay 100 \) -swap 0,-1 +delete {0}'.format(outFile))
    os.system('cp {0} {1}'.format(outFile, baseDir))

    # clean everything up
    #os.system('ls -l {}'.format(dir))
    os.system('rm {}/*'.format(dir))
    os.removedirs(dir)


# the main function, obviously
def main():
    # the location information
    l = astral.Location((_city, _region, _latitude, _longitude, _timezone, _elevation))

    # the months we have to take care of
    for year, month in getMonths():
        # get some calculations done for the sunrise and -set
        daysOfMonth = calendar.monthrange(year, month)[1]
        firstDay = datetime.date(year, month, 1)
        lastDay = datetime.date(year, month, daysOfMonth)
        startDT = l.sunrise(firstDay) + datetime.timedelta(hours=-1)
        stopDT = l.sunset(lastDay) + datetime.timedelta(days=-(daysOfMonth-1), hours=1, minutes=15)
        startTime = startDT - datetime.timedelta(minutes=(startDT.minute % 15))
        stopTime = stopDT - datetime.timedelta(minutes=(stopDT.minute % 15))

        # get the image list
        imageList = getContinuousImageSequence(startTime, stopTime, daysOfMonth)
        writeGif(imageList, startTime)


if __name__ == '__main__':
    main()
