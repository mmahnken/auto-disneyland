import requests
import sms

payload = {'segment': 'ticket', 
		   'startDate': '2022-05-31', 
		   'endDate': '2022-05-31',
}
# payload = {'segment': 'ticket', 
# 		   'startDate': '2022-06-11', 
# 		   'endDate': '2022-06-11',
# }

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = "https://disneyland.disney.go.com/availability-calendar/api/calendar"
resp = requests.get(url, params=payload, headers=headers)
resp = resp.json()
print(resp)

parks = {'DLR_CA':"California Adventure", 
		'DLR_DP': "Magic Kingdom"}

available_parks = [parks.get(p, p) for p in resp[0]['parks']]
if len(available_parks) > 0:
	park_string = ",".join(available_parks)
	sms.send_message(f"""Found Disney park availability for {payload['endDate']} at {park_string}!
-Your friendly Disney Ticket robot """, ["+15202479881", "+15202291789"])
else:
	print("CHECKED DISNEY, NO AVAILABILITY")