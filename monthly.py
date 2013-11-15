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

_city = 'Darmstadt'
_region = 'Germany'
_latitude = "49°52'N"
_longitude = "8°39'E"
_elevation = 144
_timezone = 'Europe/Berlin'

_dataDir = './'


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
        startDT = l.sunrise(firstDay) - datetime.timedelta(hours=1)
        stopDT = l.sunset(lastDay) + datetime.timedelta(hours=1)
        startTime = startDT
        stopTime = stopDT - datetime.timedelta(days=(daysOfMonth-1))


        print stopTime - startTime
    # date = datetime.date(2013,11,10)
    # print l.sunrise()
    # print l.sunrise(date)


if __name__ == '__main__':
    main()
