# This is to return the current time from the TCSC clock
#epoch convertor https://www.epochconverter.com/

import requests
import time
import webbrowser

open_time = 1489579200
#alert_time = 3000  # 10min warning
alert_time = 132600
timeLeft = 0
timer = 0 
currentTime = 0


#source URLS
application_url = 'https://tcsailing.org/harbor/application//newmember-signup/'
sailsignup_url = 'https://tcsailing.org/harbor/application/'


#the meat of the call and service
def main():
	while True:

		currentTime = time.time()  #realized the site was just using epoch, so i just grab that instead
		timeLeft = open_time - currentTime

		if (timeLeft < alert_time):
			print "its time"
			print timeLeft
			print currentTime

			send_prowl_alert()
			webbrowser.open_new(application_url)
			webbrowser.open_new(sailsignup_url)

		else:
			print "Not there yet, it's still not time " 
			print timeLeft
			print currentTime

		#sleeps the script for 5 sec
		time.sleep(5)	

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
