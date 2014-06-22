#!/usr/bin/env python
import os
import argparse

parser = argparse.ArgumentParser(description='Goes recursively through the subdirectories of a given path and uploads the pictures of a day', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--rootdir', type=str, help="Base directory from where, recursively, images are uploaded.")

args = parser.parse_args()
rootdir = args.rootdir

if not (os.path.isabs(rootdir)):
	rootdir = os.path.join(os.getcwd(), rootdir)

listOfDates = []
for root, dirs, files in os.walk(rootdir):
	if (dirs == []):
		rootSplit = root.split("/")
		day = int(rootSplit[-1])
		month = int(rootSplit[-2])
		year = int(rootSplit[-3])
		if (year > 2012) and (month <= 12) and (day <= 31):
			listOfDates.append(root)

print listOfDates
