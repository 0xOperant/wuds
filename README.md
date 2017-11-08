# WUDS
Wifi User Detection System, now with RDS back-end and Slack Alerts

This is my take on Tim Tomes' original WUDS project, which you can read more about here:   
[LaNMaSteR53.com](https://www.lanmaster53.com/2014/10/wifi-user-detection-system/)   
or the original repo:   
[BitBucket.com](https://bitbucket.org/LaNMaSteR53/wuds)

Tim is no longer actively updating, so I have ported the project here and made a few changes:   
1 - the original mac vendor lookup API is gone, so I have moved to a new provider   
2 - moved from sqlite3 to MySQL on Amazon RDS   
3 - added slack alerts   

More to come:
* web front end for SQL queries
