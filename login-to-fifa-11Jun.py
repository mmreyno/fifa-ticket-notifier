#!/usr/bin/env python

import urllib
import urllib2
import json
import smtplib

# two passes as a json dict to get to nested values
json_data = urllib2.urlopen('https://fwctickets.fifa.com/TopsAkaCalls/Calls.aspx/getRefreshChartAvaDem?l=en&c=BRA')
content = json_data.read()
games = json.loads(content)
pass_two = json.loads(games['d']['data'])

# games that are required (need, in order: FINAL, BH 1/2, SP 1/2, RJ 1/4)
# need = 441,442,443,444,427,428,429,430,420,421,422,423,399,400,401,402
# for others =  (in order RIO 1/8, SP 1/8, SP GROUP): 343,344,345,346,378,379,380,381,154,155,156,157,245,246,247,248,322,323,324,325
# test = 259
desired_games = [441,442,443,444,427,428,429,430,420,421,422,423,399,400,401,402,343,344,345,346,378,379,380,381,154,155,156,157,245,246,247,248,322,323,324,325,259]

# iterate over the games to see which ones have available tickets
for i in desired_games:
    if int(pass_two['BasicCodes']['PRODUCTPRICES'][i]['Quantity']) > 0:
        # send an email if the value is above 0
        successful_game = pass_two['BasicCodes']['PRODUCTPRICES'][i]['PRPProductId']
        successful_cat = pass_two['BasicCodes']['PRODUCTPRICES'][i]['PRPCategoryId'] 
        number_of_tickets = pass_two['BasicCodes']['PRODUCTPRICES'][i]['Quantity']       
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 587
        password = ''
         
        sender = ''
        recipient = ''
        subject = number_of_tickets + ' TICKETS FOR ' + successful_game + ' CAT' + successful_cat
        body = 'Go buy it!' 
         
        "Sends an e-mail to the specified recipient."
         
        body = "" + body + ""
         
        headers = ["From: " + sender,
                   "Subject: " + subject,
                   "To: " + recipient,
                   "MIME-Version: 1.0",
                   "Content-Type: text/html"]
        headers = "\r\n".join(headers)
         
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(sender, password)
         
        session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
        session.quit()                   




