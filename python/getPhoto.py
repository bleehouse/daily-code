import requests

payload = {'tags': 'nature'} 
r = requests.get('https://api.flickr.com/services/feeds/photos_public.gne?tags=nature', params=payload)

xmlStr = ""

# http://stackoverflow.com/questions/14630288/unicodeencodeerror-charmap-codec-cant-encode-character-maps-to-undefined
for chunk in r.iter_content(chunk_size=128):
    xmlStr = xmlStr + chunk.decode("utf-8").encode('cp949', 'replace').decode('cp949')

print(xmlStr)
