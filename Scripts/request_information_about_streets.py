import json, requests, re, string, xmltodict

def street_info(street_name, city_name):
	require_url = ('https://maps.googleapis.com/maps/api/place/textsearch'
											+ '/xml?'
											+ 'query=' + street_name.replace(' \n','') + '+' + city_name
											+ '&key='+'AIzaSyB8PZ4UFS30x88lGiz2W3a4ERmAEI3rpPw')
	util_street_info = {}

	content = requests.get(require_url).content
	json_content = json.loads(json.dumps(xmltodict.parse(content)))['PlaceSearchResponse']
	
	if json_content.has_key('result') == False:
		print require_url
		return '{"not find"}'
	if len(json_content) == 2:
		json_results = json_content['result']
	else:
		json_results = json_content['result'][0]
	
	util_street_info.update({'id':json_results['id']})
	util_street_info.update({'name':json_results['name']})
	util_street_info.update({'place_id':json_results['place_id']})
	util_street_info.update({'geometry':{'lat':json_results['geometry']['location']['lat'],'lng':json_results['geometry']['location']['lng']}})

	return util_street_info

file_in = open('../street_names','r')
file_out = open('../street_info_from_google','w')
count = 0
for line in file_in:
	count +=1
	file_out.write(str(street_info(line,'joinville')) + '\n')
	print('done - ' + str(count))
