from flask import Flask, request, Response, g, stream_with_context
from slackclient import SlackClient
import os
import sqlite3 as lite
from config import *

app = Flask(__name__)

@app.route('/wuds', methods=['POST'])
def wuds_parse():
    if request.form.get('token') == SLACK_TOKEN and request.form.get('user_id') == USER_ID:
        text = request.form.get('text')
        if text:
            fields = text.split()
            command = fields[0]
            query = fields[1]
            con = lite.connect(LOG_FILE)
            con.row_factory = lite.Row
            cur = con.cursor()
            if command == "mac":
                cur.execute('select distinct ssid from probes where mac = ? and ssid != "<None>"', [query])
                rows = cur.fetchall();
                if rows:
                    def generate():
                        for row in rows:
                            yield ','.join(row) + ' (was probed by ' + query + ')\n'
                    return Response(generate()), 200
                else:
                    return "sorry, MAC: " + query + " hasn't probed any networks.", 200
            elif command == "ssid":
                cur.execute('select distinct mac, oui from probes where ssid = ?', [query])
                rows = cur.fetchall();
                if rows:
                    def generate():
                        for row in rows:
                            yield ' - OUI: '.join(row) + ' - (probed for ' + query + ')\n'
                    return Response(generate()), 200
                else:
                    return "sorry, SSID: " + query + " is not in the database.", 200
            elif command == "whitelist":
                oui = fields[2]
                comment = fields[3]
                cur.execute('insert into whitelist (mac, oui, comment) values (?, ?, ?)', (query, oui, comment))
                con.commit()
                return "MAC " + query + " added to the whitelist.", 200
        else:
            return "Command not found, please try again with [SSID], [MAC], [WHITELIST], or [SELECT].", 200
    else:
        return "Unauthorized. Contact your workspace admin for access.", 401

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
