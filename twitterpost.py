from twython import Twython
import json

def push_post(imageFilepath, post):
	APP_KEY = 'your key here'
	APP_SECRET = 'your secret here'

	OAUTH_TOKEN = 'your oauth token here'
	OAUTH_TOKEN_SECRET = 'your oauth secret here'

	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	photo = open(imageFilepath,  'rb')
	if (photo is None) :
		return False
	else :
		response = twitter.upload_media(media=photo)
		twitter.update_status(status=post, media_ids=[response['media_id']])
		return True
