import argparse
import datetime
import os
import imgurHandler

class imgurBackup(object):
	"""Uploads the content of a date-separated path to Imgue"""
	def __init__(self, imgur, path):
		super(imgurBackup, self).__init__()
		self.imgur = imgur
		self.path = self.normalizePath(path)
		self.date = self.generateDateFromPath(self.path)
		self.listOfJgs = self.getJpgsInDirectory(self.path)
		self.album = self.imgur.createFairAlbum(self.date)
		self.imgur.uploadJpgsToAlbum(self.listOfJgs, self.album)
		self.writeAlbumInfoFile()

	def normalizePath(self, path):
		if not (os.path.isabs(path)):
			path = os.path.join(os.getcwd(), path)
		return os.path.normpath(path)
	
	def generateDateFromPath(self, path):
		splitted_path = path.split("/")
		current_day = splitted_path[-1]
		current_month = splitted_path[-2]
		current_year = splitted_path[-3]
		return datetime.date(int(current_year), int(current_month), int(current_day))

	def getJpgsInDirectory(self, path):
		return sorted([os.path.join(path, file) for file in os.listdir(path) if file.endswith(".jpg")])

	def writeToFile(self, file, data):
		with open(file, 'w') as outputfile:
			for entry in data:
				outputfile.write(entry + "\n")

	def writeAlbumInfoFile(self):
		text = ["The individual pictures used too much space on the server's harddisk.", "We moved them.", "You can find them here: " + self.album.link, "Additionally, there's an offline backup.", "Just contact the author to get them!", "Cheers, Andreas"]
		self.writeToFile(os.path.join(self.path, "where_are_the_pictures.txt"), text) 

def main(args):
	imgur = imgurHandler.imgurHandler(args.initialize, args.imgur_credentials_json)
	path = args.target_dir
	imgurBackup(imgur, path)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Uploads pictures into albums on imgur', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--initialize', action='store_true', help="Create new access_token and refresh_token")
	parser.add_argument('--imgur-credentials-json', type=str, default="imgur_credentials.json", help="File with login info of imgur.")
	parser.add_argument('--target-dir', type=str, help="Directory with pictures to upload.")
	args = parser.parse_args()

	main(args)
