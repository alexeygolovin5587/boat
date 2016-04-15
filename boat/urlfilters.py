from urllib import urlencode

from hash_table import boatsArray

# genrate one url of cruise_ireland
def gen_cruise_ireland(url, data, form_values):
	params = {
		"show_cruise":1,
		"cruise_option":2,
		"boat":data["BoatID"],
		"search_duration":form_values["nights"],
		"submit_button.x":37,
		"submit_button.y":10,
		"submit_button":"SEARCH"
	}
	return url+'?'+urlencode(params)+"&search_date="+form_values["date"],

# genrate one url of emeraldstar
def gen_emeraldstar(url, data, form_values):
	new_url = url + data['BoatID'] + "/cruises-and-prices?"

	dateArr = form_values['date'].split('/')
	new_date = [dateArr[2], dateArr[1], dateArr[0]]

	params = {
		"filters_applied":1,
		"f[0]": "nights:" + str(form_values["nights"]),
		"f[1]": "date:during|" + "-".join(new_date), 
		"f[2]": "destination:21",
	}

	return new_url+urlencode(params)+"#lb-content-tabs"

# genrate one url of silverlinecruisers
def gen_silver(url, data, form_values):
	new_url = url + data['BoatID'] + "/"
	temp_date = form_values['date'].split('/')
	params = {
		"wc_bookings_field_duration": form_values["nights"],
		"wc_bookings_field_start_date_year": int(temp_date[2]), 
		"wc_bookings_field_start_date_month": int(temp_date[1]),
		"wc_bookings_field_start_date_day": int(temp_date[0])
	}
	res = {new_url:urlencode(params) + data['slID']}
	return res

# generate possible urls of cruise_ireland
def gen_cruise_ireland_urls(form_values):
	urls = []
	postIDs = []
	for domainUrl in boatsArray[form_values["Marinas"]]:
		# cruise-ireland
		if domainUrl == "http://cruise-ireland.com/book-now/":
			for boat in boatsArray[form_values["Marinas"]][domainUrl]:
				urls.append(''.join(gen_cruise_ireland(domainUrl, boat, form_values)))
				postIDs.append(boat['PostID'])
	return [urls, postIDs]

# generate possible urls of emeraldstar
def gen_emeraldstar_urls(form_values):
	urls = []
	postIDs = []
	for domainUrl in boatsArray[form_values["Marinas"]]:
		#emeratldstar
		if domainUrl == "http://www.emeraldstar.ie/boats/":
			for boat in boatsArray[form_values["Marinas"]][domainUrl]:
				urls.append(''.join(gen_emeraldstar(domainUrl, boat, form_values)))
				postIDs.append(boat['PostID'])
	return [urls, postIDs]

# generate possible urls of silverlinecruisers
def gen_silver_urls(form_values):
	urls = dict()
	postIDs = []
	for domainUrl in boatsArray[form_values["Marinas"]]:
		#emeratldstar
		if domainUrl == "http://silverlinecruisers.com/product/":
			for boat in boatsArray[form_values["Marinas"]][domainUrl]:
				urls.update(gen_silver(domainUrl, boat, form_values))
				postIDs.append(boat['PostID'])

	return [urls, postIDs]
