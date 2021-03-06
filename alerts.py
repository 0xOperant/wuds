from config import *

'''
Each module must receive **kwargs as a parameter. The kwargs variable is a dictionary
consisting of all the data extracted from the probe request. Each module name must
start with 'alert_' and have a matching variable in config.py for enabling/disabling.
Configurable module options may be defined in config.py.
'''

from email.mime.text import MIMEText
import smtplib

def alert_sms(**kwargs):
    msg = MIMEText('WUDS proximity alert! A foreign device (%s - %s) has been detected on the premises.' % (kwargs['bssid'], kwargs['oui']))
    server = smtplib.SMTP(SMTP_SERVER)
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    server.sendmail(SMTP_USERNAME, SMS_EMAIL, msg.as_string())
    server.quit()

import urllib
import urllib2

def alert_pushover(**kwargs):
    msg = 'A foreign device has been detected nearby: (%s, %s, %sdbm, %s)' % (kwargs['bssid'], kwargs['oui'], kwargs['rssi'], kwargs['essid'])
    url = 'https://api.pushover.net/1/messages.json'
    payload = {'token': PUSHOVER_API_KEY, 'user': PUSHOVER_USER_KEY, 'message': msg}
    payload = urllib.urlencode(payload)
    resp = urllib2.urlopen(url, data=payload)

def alert_slack(**kwargs):
    msg = '{"text": "A foreign device has been detected nearby:\n(%s , %s , %sdbm, %s)"}' % (kwargs['bssid'], kwargs['oui'], kwargs['rssi'], kwargs['essid'])
    url = WEBHOOK_URL
    resp = urllib2.urlopen(url, data=msg)
    
def alert_hubot(**kwargs):
    hubot_alert = ':wifi: *WUDS Alert:* A foreign device has been detected nearby:\n(%s, %s, %sdbm, %s)' % (kwargs['bssid'], kwargs['oui'], kwargs['rssi'], kwargs['essid'])
    hubot_msg = {'token':HUBOT_TOKEN,'text':hubot_alert}
    hubot_url = HUBOT_URL
    hubot_payload = urllib.urlencode(hubot_msg)
    hubot_resp = urllib2.urlopen(hubot_url, data=hubot_payload)

def status_alert_hubot(hubot_status):
    hubot_msg = {'token':HUBOT_TOKEN,'text':hubot_status}
    hubot_url = HUBOT_URL
    hubot_payload = urllib.urlencode(hubot_msg)
    hubot_resp = urllib2.urlopen(hubot_url, data=hubot_payload)
