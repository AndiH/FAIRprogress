import pyimgur
import json
import webbrowser
import argparse
import datetime
import os


def jsonParser(file):
	data_file = open(file)
	data = json.load(data_file)
	data_file.close()
	return data

def jsonWriter(file, data):
	with open(file, 'w') as outputfile:
		json.dump(data, outputfile)

def initializeTokens(im, credentials):
	auth_url = im.authorization_url('pin')
	webbrowser.open(auth_url)
	pin = raw_input("What is the pin? ") # Python 2x
	access_token, refresh_token = im.exchange_pin(pin)
	credentials["access_token"] = access_token
	credentials["refresh_token"] = refresh_token
	return credentials

def updateAccessToken(im, credentials):
	credentials["access_token"] = im.refresh_access_token()
	return credentials

def writeToFile(file, data):
	with open(file, 'w') as outputfile:
		for entry in data:
			outputfile.write(entry + "\n")

def main(args):
	imgur_credential_file = args.imgur_credentials_json
	credentials = jsonParser(imgur_credential_file)
	im = pyimgur.Imgur(credentials["clientid"], credentials["clientsecret"])
	if (args.initialize):
		credentials = initializeTokens(im, credentials)
	if not (args.initialize):
		im.refresh_token = credentials["refresh_token"]
		credentials = updateAccessToken(im, credentials)

	jsonWriter(imgur_credential_file, credentials)

	path = args.target_dir
	if not (os.path.isabs(path)):
		path = os.path.join(os.getcwd(), path)
	path = os.path.normpath(path)
	splitted_path = path.split("/")
	# print splitted_path
	current_day = splitted_path[-1]
	current_month = splitted_path[-2]
	current_year = splitted_path[-3]
	# print current_day, current_month, current_year
	date = datetime.date(int(current_year), int(current_month), int(current_day))

	album = im.create_album("FAIRprogress of " + date.strftime('%Y-%m-%d'), "Raw pictures used to generate the gif located at http://fair.andreasherten.de/images/" + current_year + "/" + current_month + "/" + current_day + ".")

	jpgs_in_current_directory = [os.path.join(path, file) for file in os.listdir(path) if file.endswith(".jpg")]
	# print jpgs_in_current_directory
	images = []
	for jpg in jpgs_in_current_directory:
		images.append(im.upload_image(jpg, title=jpg.split("/")[-1]))
	album.add_images(images)
	
	text = ["The individual pictures used too much space on the server's harddisk.", "We moved them.", "You can find them here: " + album.link, "Additionally, there's an offline backup.", "Just contact the author to get them!", "Cheers, Andreas"]

	writeToFile(os.path.join(path, "where_are_the_pictures.txt"), text) 

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Uploads pictures into albums on imgur', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--initialize', action='store_true', help="Create new access_token and refresh_token")
	parser.add_argument('--imgur-credentials-json', type=str, default="imgur_credentials.json", help="File with login info of imgur.")
	parser.add_argument('--target-dir', type=str, help="Directory with pictures to upload.")
	args = parser.parse_args()

	main(args)
