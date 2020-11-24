import re
import base64
import requests

web_url = 'https://www.raspberrypi.org/community/'

f = requests.get(web_url)

html = f.text


print ('URL_FIND ==>' + web_url)
