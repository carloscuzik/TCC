import json, requests

names_ids = {}
names_ids.update({'RockFeller':'ChIJkdEaSj-w3pQRUhf00nVYu5g'})
names_ids.update({'Magrathea_Labs':'ChIJG6B5DC6w3pQRHM-7HtOV7lU'})

def rote_info(origin, destination):
	return requests.get("https://maps.googleapis.com/maps/api/directions/json?"
											+ "origin=place_id:" + names_ids[origin]
											+ "&destination=place_id:" + names_ids[destination]
											+ "&key=AIzaSyDNFfzulwTdNST376L6sCPaMtvCBYNPbR0").content

print rote_info('RockFeller','Magrathea_Labs')