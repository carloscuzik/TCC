import json, requests, re, string

def street_info(street_name, city_name):
	require_url = ('https://maps.googleapis.com/maps/api/place/textsearch'
											+ '/json?'
											+ 'query=' + street_name.sub('\n','') + '+' + city_name
											+ '&key='+'AIzaSyB8PZ4UFS30x88lGiz2W3a4ERmAEI3rpPw')
	
	content = requests.get(require_url).content
	json_content = json.loads(content)
	print require_url
	# json_results = json_content['results']
	
	# util_street_info = {}

	# util_street_info.update({'id':json_results['id']})
	# util_street_info.update({'name':json_results['name']})
	# util_street_info.update({'place_id':json_results['place_id']})
	# util_street_info.update({'geometry':{'lat':json_results['geometry']['location']['lat'],'lng':json_results['geometry']['location']['lng']}})

	# return util_street_info

file_in = open('../street_names','r')
file_out = open('../street_info_from_google','w')
count = 0
for line in file_in:
	count +=1
	file_out.write(str(street_info(line,'joinville')) + '\n')
	print('done - ' + str(count))
