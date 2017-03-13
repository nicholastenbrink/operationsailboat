# This is to return the current time from the TCSC clock
#epoch convertor https://www.epochconverter.com/

import urllib
import urllib2
import requests
import time
import webbrowser


open_time = 1489579200
#alert_time = 3000  # 10min warning
alert_time = 132600
timeLeft = 0
timer = 0 


#source URLS
url_source = "https://tcsailing.org//harbor//wp-content//themes//tcsc2017//countdown//timenow.php"
application_url = 'https://tcsailing.org/harbor/application//newmember-signup/'
sailsignup_url = 'https://tcsailing.org/harbor/application/'


#dummy data to make the server think it is being called by a human
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'  #we need to fake a human other wise we get a 403 forbidden return
values = {'name': 'Leroy Jenkins',
          'location': 'Moon',
          'language': 'Elvish' }
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)

#the meat of the call and service
def main():
	while True:
		
		#this is where the request is
		req = urllib2.Request(url_source, data, headers)
		response = urllib2.urlopen(req)
		
		#this is the return from timenow
		timer = int(response.read())

		#this checks how much time left
		timeLeft = open_time - timer

		if (timeLeft < alert_time):
			print "its time"
			print timeLeft
			print timer
			send_prowl_alert()
			webbrowser.open_new(application_url)
			webbrowser.open_new(sailsignup_url)


		else:
			print "Not there yet, it's still " 
			print timeLeft
			print timer


		#sleeps the script for min
		time.sleep(600)	


#prowl notification
def send_prowl_alert():
    prowl_url = 'https://prowlapp.com/publicapi/add'
    prowl_api_keys = [
        'xxxxxxx'  # nick
        ]
    for prowl_user_key in prowl_api_keys:
        payload = {
                    'apikey': prowl_user_key,
                    'application': 'Sailing Signup',
                    'description': 'Go sign up!\n{}'.format(application_url),
                    'priority': 2,
                   }
        requests.get(prowl_url, params=payload)

main()
