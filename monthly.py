#!/usr/bin/python
# -*- coding: utf-8

#
#  Generate the monthly FAIRprogress
# ------------------------------------

# import stuff
import sys, os          # system functions (like exit, file handling)
import datetime         # time functions
import astral           # sunrise stuff

_city = 'Darmstadt'
_region = 'Germany'
_latitude = "49°52'N"
_longitude = "8°39'E"
_elevation = 144
_timezone = 'Europe/Berlin'

def main():
    l = astral.Location((
        _city,
        _region,
        _latitude,
        _longitude,
        _timezone,
        _elevation
    ))
    date = datetime.date(2013,11,10)
    print l.sunrise()
    print l.sunrise(date)


if __name__ == '__main__':
    main()
