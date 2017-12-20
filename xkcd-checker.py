import requests
import re
import os
from tinydb import TinyDB, Query
# /usr/bin/env python
from twilio.rest import Client

account_sid = os.envorin.get('ACCOUNT_SID')
auth_token = os.envorin.get('AUTH_TOKEN')

client = Client(account_sid, auth_token)

db = TinyDB('db.json')
db.insert({'edition': 1915});

res = requests.get('https://www.xkcd.com')
# if res.status == 200:
text = res.text
match = re.search(r'https:\/\/xkcd\.com\/(\d+)', text, flags=0)
if match:
	current = int(match.group()[-4:])
	Latest = Query()
	fromDb = db.search(Latest.edition == current)
	if len(fromDb) == 0:
		# do the thing
		client.api.account.messages.create(
		    to= os.envorin.get('PHONE_NUMBER'),
		    from_=os.envorin.get('FROM_NUMBER')
		    body="New XKCD alert: https://www.xkcd.com/{0}".format(current)
	    )
		db.insert({'edition': current})