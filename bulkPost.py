import os
import json
import urllib
import pprint
from access_token import *

# get Facebook access token from environment variable
ACCESS_TOKEN = access_token
ids = "673366896048573"
# build the URL for the API endpoint
host = "https://graph.facebook.com/"
path = ids+"/feed?fields=comments{id,message,like_count,created_time,from,comment_count}"
token = urllib.urlencode({"access_token": ACCESS_TOKEN})

url = "{host}{path}&{params}".format(host=host, path=path, params=token)

# open the URL and read the response
resp = urllib.urlopen(url).read()

# convert the returned JSON string to a Python datatype 
result = json.loads(resp)

# display the result
pprint.pprint(result)