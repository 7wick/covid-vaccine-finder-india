import requests
import os
import json

# inputs

date = "04-05-2021"     # will show you all the available centres, 7 days from this date
age = 25        # enter age of the person to be vaccinated
# state_name = "uttar pradesh"        # enter your state name
# district_name = "gorakhpur"        # enter your district name
state_name = "west bengal"        # enter your state name
district_name = "kolkata"        # enter your district name

'''
For Andaman and Nicobar Islands enter state name state_name = "Andaman and Nicobar Islands" 
For Dadra and Nagar Haveli enter state name state_name = "Dadra and Nagar Haveli" 
For Daman and Diu enter state name state_name = "Daman and Diu" 
For Jammu and Kashmir enter state name state_name = "Jammu and Kashmir" 
'''


#code

try:
    unchanged_states = ["Andaman and Nicobar Islands", "Dadra and Nagar Haveli", "Daman and Diu", "Jammu and Kashmir"]
    if state_name not in unchanged_states:
        state_name = state_name.title()

    states = json.loads(os.popen("curl --silent https://cdn-api.co-vin.in/api/v2/admin/location/states").read())['states']
    state_id = next(item for item in states if item["state_name"] == state_name)['state_id']
except Exception as err:
    print("Invalid state_name. Enter it correctly. \nTip: Might be a spelling mistake!")
    raise SystemExit(err)

try:
    district_url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{0}".format(str(state_id))
    districts = json.loads(os.popen("curl --silent {0}".format(district_url)).read())['districts']
    district_id = next(item for item in districts if item["district_name"] == district_name.capitalize())['district_id']
except Exception as err:
    print("\nInvalid district_name. Enter it correctly!")
    raise SystemExit(err)

try:
    response = requests.get(
        "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict",
        params={
            'district_id': district_id,
            'date': date
        },
    )
    total_available_centres = 0
    for centre in response.json()["centers"]:
        for details in centre["sessions"]:
            result = dict()
            if details['available_capacity'] > 0 and details["min_age_limit"] <= age:
                total_available_centres += 1
                result["name"] = centre["name"]
                result["block_name"] = centre["block_name"]
                result["pincode"] = centre["pincode"]
                result["min_age_limit"] = details["min_age_limit"]
                result["date"] = details["date"]
                result["available_capacity"] = details["available_capacity"]
                print(result, "\n")

    if total_available_centres > 0:
        print("\nTotal available centres: ", total_available_centres)
        print("\nRegister your slot at https://www.cowin.gov.in/home")
    else:
        print("\nNo vaccines available in this district, for the given age!")

except Exception as err:
    print("\nUnexpected Error. Kindly retry a couple of times!\nIf the issue persist, contact the admin")
    raise SystemExit(err)