import json, xmltodict, requests

locals_address = {}
locals_address.update({'RockFeller'     : 'ChIJkdEaSj-w3pQRUhf00nVYu5g'})
locals_address.update({'Magrathea_Labs' : 'ChIJG6B5DC6w3pQRHM-7HtOV7lU'})
locals_address.update({'Udesc-CCT' : 'ChIJ6SrUgKSv3pQR4RK0Imh29q8'})

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
											+ "&departure_time:" + "now"
											+ "&key=" + my_key[api_mode])

	content = requests.get(require_url).content
	
	if(return_format=='json'):
		steps = ((json.loads(content)['routes'][0])['legs'][0])['steps']
	else:
		steps = json.loads(json.dumps(xmltodict.parse(content)))['DirectionsResponse']['route']['leg']['step']
	
	for step in steps:
		print str(float(step['distance']['value']) / float(step['duration']['value']))

rote_info('Udesc-CCT','Magrathea_Labs','car','directions','xml')