import os
import json
import urllib
import pprint

# get Facebook access token from environment variable
ACCESS_TOKEN = "EAACEdEose0cBABnjvubPKRVMKheRXuUE751QLfoYmSBJPL6Fw6AGGEkQgvQmhDEQ8rkQd1Df0n3ThOl9q3abJR5EYBzLjBMZBiuXoTvhgY07VlG9Q5i5JjCHSkfl6cNcOnDMX0gBNcGpgOiclZACiLG131Bc3rJH6WvM7o3RZAUlJG98zeBBmBkyEeZBGV4ZD"
ids = "1212796532105604"
# build the URL for the API endpoint
host = "https://graph.facebook.com/"
path = ids+"?fields=comments{id,message,like_count,comment_count}"
token = urllib.urlencode({"access_token": ACCESS_TOKEN})

url = "{host}{path}&{params}".format(host=host, path=path, params=token)

# open the URL and read the response
resp = urllib.urlopen(url).read()

# convert the returned JSON string to a Python datatype 
me = json.loads(resp)

# display the result
pprint.pprint(me)