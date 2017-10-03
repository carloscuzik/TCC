import json, requests

locals_address = {}
locals_address.update({'RockFeller'     : 'ChIJkdEaSj-w3pQRUhf00nVYu5g'})
locals_address.update({'Magrathea_Labs' : 'ChIJG6B5DC6w3pQRHM-7HtOV7lU'})

my_key = {}
my_key.update({'directions'     : 'AIzaSyDNFfzulwTdNST376L6sCPaMtvCBYNPbR0'})

api_request = {}
api_request.update({'directions':'directions'})

forma_request = {}
forma_request.update({'json' : 'json'})
forma_request.update({'xml'  : 'xml' })

mode = {}
mode.update({'car' : 'driving'})
mode.update({'bus' : 'transit'})

def rote_info(origin, destination,mode_go,api_mode,return_format):
	require_url = ("https://maps.googleapis.com/maps/api/"
											+ api_request[api_mode]
											+ '/' + forma_request[return_format] +'?'
											+ "origin=place_id:" + locals_address[origin]
											+ "&destination=place_id:" + locals_address[destination]
											+ "&mode=" + mode[mode_go]
											+ "&key=" + my_key[api_mode])
	
	content = requests.get(require_url).content
	json_content = json.loads(content)

	json_routs = json_content['routes'][0]

	json_legs = json_routs['legs'][0]
	
	for step in json_legs['steps']:
		print str(float(step['distance']['value']) / float(step['duration']['value'])) + ':' + step['html_instructions']

print rote_info('RockFeller','Magrathea_Labs','car','directions','json')