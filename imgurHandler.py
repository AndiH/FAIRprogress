import pyimgur
import json
import webbrowser

class imgurHandler(object):
	'''Interface to pyimgur for my needs: Reads in credentials from a json file and updates the tokens. Also offers a special method for my case (createFairAlbum()).'''
	def __init__(self, initialize, credential_file):
		super(imgurHandler, self).__init__()
		self.credentials = self.jsonParser(credential_file)
		self.im = pyimgur.Imgur(self.credentials["clientid"], self.credentials["clientsecret"])
		if (initialize):
			self.credentials = self.initializeTokens(self.im, self.credentials)
		if not (initialize):
			self.im.refresh_token = self.credentials["refresh_token"]
			self.credentials["access_token"] = self.im.refresh_access_token()
		self.jsonWriter(credential_file, self.credentials)

	def jsonParser(self, file):
		data_file = open(file)
		data = json.load(data_file)
		data_file.close()
		return data

	def jsonWriter(self, file, data):
		with open(file, 'w') as outputfile:
			json.dump(data, outputfile)

	def initializeTokens(self):
		auth_url = self.im.authorization_url('pin')
		webbrowser.open(auth_url)
		pin = raw_input("What is the pin?")
		access_token, refresh_token = self.im.exchange_pin(pin)
		self.credentials["access_token"] = access_token
		self.credentials["refresh_token"] = refresh_token

	def createFairAlbum(self, date):
		return self.im.create_album("FAIRprogress of " + date.strftime('%Y-%m-%d'), "Raw pictures used to generate the gif located at http://fair.andreasherten.de/images/" + str(date.year) + "/" + str(date.month).zfill(2) + "/" + str(date.day).zfill(2) + ".")

	def uploadJpgsToAlbum(self, jpgs, album):
		images = []
		for jpg in jpgs:
			images.append(self.im.upload_image(jpg, title=jpg.split("/")[-1]))
		album.add_images(images)
