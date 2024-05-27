import requests
from secret import *

resp = requests.post('https://textbelt.com/text', {
  'phone': PHONE,
  'message': MESSAGE,
  'key': KEY,
})

print(resp.json())

