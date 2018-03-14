import requests

vin=raw_input('Enter VIN: ')
client_id='F06D279AF097E71195F69F6685914432'
secret='AeBD6ZaT9VnPxGEO37Guig'
##(token generation) print ('\nHere is your 1 hour token:  '+requests.post("https://api.dmotorworks.com/auth2/tokens", data={"grant_type":"client_credentials"}, auth=(client_id, secret)).json()["access_token"])
token=(requests.post("https://api.dmotorworks.com/auth2/tokens", data={"grant_type":"client_credentials"}, auth=(client_id, secret)).json()["access_token"])

dr=requests.get(("https://api.dmotorworks.com/oems/vehicles/%s?_token=%s&includeFeatures=true&includeOptions=true" % (vin,token)))

print("RAW URL (copy to browser to see subOptions): \n"+"https://api.dmotorworks.com/oems/vehicles/%s?_token=%s&includeFeatures=true&includeOptions=true" % (vin,token))

print ("\n \nOPTION VALUES:")
g=0
option_value_total=0
option_codes=[]
opt_value=0
try:
	for i in dr.json()["optionPackages"]:
		opt_desc=dr.json()["optionPackages"][g]["description"]
		try:
			opt_value=dr.json()["optionPackages"][g]["msrp"]
			option_value_total=dr.json()["optionPackages"][g]["msrp"]+option_value_total
		except:
			pass
		print (opt_desc + " "+str(opt_value))
		try: 
			option_codes.append(dr.json()["optionPackages"][g]['code'])
		except:
			pass
		g=g+1
	print ("TOTAL OPTION VALUE: " + str(option_value_total)+"\n")
except:
	pass
print (option_codes)
print(dr.json()["vin"])
print(dr.json()["modelYear"])
print(dr.json()["make"])
print(dr.json()["model"])
try:
	print(dr.json()["trimLevel"])
except:
	print('base')
