import requests
import json
request=requests.get("http://api.plos.org/search?q=title:'Drosophila' AND body:'RNA'&fl=id&start=100&rows=100")

'getting the string data using text method'

request_string=request.text



'getting dict data from url using json()'
request_json=request.json()



print(type(request_string))