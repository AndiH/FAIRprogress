import imgurBackup, imgurHandler
import argparse

def main(args):
	imgur = imgurHandler.imgurHandler(args.initialize, args.imgur_credentials_json)
	path = args.target_dir
	imgurBackup.imgurBackup(imgur, path)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Uploads pictures into albums on imgur', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--initialize', action='store_true', help="Create new access_token and refresh_token")
	parser.add_argument('--imgur-credentials-json', type=str, default="imgur_credentials.json", help="File with login info of imgur.")
	parser.add_argument('--target-dir', type=str, help="Directory with pictures to upload.")
	args = parser.parse_args()

	main(args)
