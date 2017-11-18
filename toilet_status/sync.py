import urllib2
import json

server_host="192.168.1.106"

def sync_toilet_status(toilet, available):
    toilet_id = toilet.get("id")
    data = {
        "available": available 
    }
    headers = {'Content-Type': 'application/json'}
    request = urllib2.Request(url='http://'+server_host+':5000/toilets/'+str(toilet_id), headers=headers, data=json.dumps(data))
    request.get_method = lambda: 'PUT'
    response = urllib2.urlopen(request)
    return response.read()

