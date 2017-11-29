from flask import Flask, request, Response, g, stream_with_context
from slackclient import SlackClient
import os
import sqlite3 as lite
from config import *

app = Flask(__name__)

@app.route('/wuds_ssid', methods=['POST'])
def wuds_ssid():
    if request.form.get('token') == SLACK_TOKEN and request.form.get('user_id') == USER_ID:
        text = request.form.get('text')
        if text:
            con = lite.connect(LOG_FILE)
            con.row_factory = lite.Row
            cur = con.cursor()
            cur.execute('select distinct mac, oui from probes where ssid = ?', [text],)
            rows = cur.fetchall();
            if rows:
                def generate():
                    for row in rows:
                        yield ' - OUI: '.join(row) + ' - (probed for ' + text + ')\n'
                return Response(generate()), 200
            else:
                return "sorry, SSID: " + text + " is not in the database.", 200
        else:
            return "Please enter an SSID.", 200
    else:
        return "Unauthorized.", 401

@app.route('/wuds_mac', methods=['POST'])
def wuds_mac():
    if request.form.get('token') == SLACK_TOKEN and request.form.get('user_id') == USER_ID:
        text = request.form.get('text')
        if text:
            con = lite.connect(LOG_FILE)
            con.row_factory = lite.Row
            cur = con.cursor()
            cur.execute('select distinct ssid from probes where mac = ? and ssid != "<None>"', [text],)
            rows = cur.fetchall();
            if rows:
                 def generate():
                     for row in rows:
                         yield ','.join(row) + ' (was probed by ' + text + ')\n'
                 return Response(generate()), 200
            else:
                return "sorry, MAC: " + text + " hasn't probed any networks.", 200
        else:
            return "Please enter a MAC address.", 200
    else:
        return "Unauthorized.", 401


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
