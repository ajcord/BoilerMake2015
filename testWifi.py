from twython import Twython
import json

APP_KEY = '4Rye2VvrGTaPDlSmxwxgwU1gQ'
APP_SECRET = 'ddCbtpCs2ePsRXcriSGwJGrmrzZKhwSYVFq1MdxML3iKwsJfnV'

OAUTH_TOKEN = '3911053409-OxVKx19eZcLz3fkhUeJyli8En2tNKi2nCQzNoQW'
OAUTH_TOKEN_SECRET = 'OOuk4Czrbv4E1dNpUWF2uiQwj3lzXdcUHl9Q3DPHa1RhR'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitter.update_status(status='WiFi Test')