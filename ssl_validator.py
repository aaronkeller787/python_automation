from settings import *
import datetime
from datetime import date, timedelta
import ssl
import OpenSSL
import smtplib

def get_SSL_Expiry_Date(host, port):

    date_list = []
    expired_domains = {}
    renew_domains = {}

    cert = ssl.get_server_certificate((host, port))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)

    byte_date = x509.get_notAfter()
    valid_date = byte_date.decode()
    steralized_date = valid_date[:8]

    for i in steralized_date:
        date_list.append(i)

    date_list.insert(4,'-')
    date_list.insert(7,'-')

    convert_date_string = ''.join(date_list)
    date_str = convert_date_string
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')

    #print('Expiry Date:', date_obj.date())

    now = datetime.datetime.today()
    #print('Today is:',now.date())
    
    almost_expired = (now + timedelta(days=45))
    past = (now - timedelta(days=1))

    if date_obj < now:
        print('Expired')
        expired_domains[s] = date_obj.date()
    elif date_obj < almost_expired and date_obj > past:
        print('Renew')
        renew_domains[s] = date_obj.date()
    else:
        print('Nothing needed')
  
    for r in renew_domains:
        f = open('domain_work.txt', 'a')
        f.write('Renew: ' + r)
        f.write(date_str)
        f.write('\n')
        f.write(r)
        f.close
    
    for e in expired_domains: 
        f = open('domain_work.txt', 'a')
        f.write('Expired: ' + e +  '\n')
        f.write(date_str)
        f.write('\n')
        f.close

f = open('domain_work.txt', 'w').close()

def mailme():

    filename = 'domain_work.txt'
    with open(filename, 'r') as filename:
        text = filename.read()

    SERVER_NAME=SERVERNAME
    SERVER_PORT=SERVERPORT
    USER_NAME=USERNAME
    PASSWORD=PASSWRD
    SUBJECT=SUB
    #print('Connecting...')
    server = smtplib.SMTP(SERVER_NAME, SERVER_PORT)
    #print('Connected...')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(USER_NAME, PASSWORD)
    message = 'Subject: {}\n\n{}'.format(SUBJECT, text)
    server.sendmail(SENDER, RECEIVER, message)
    server.quit()

file = open('sites.txt', 'r')
sites = file.read()
site_list = sites.split('\n')
file.close()
site_list.remove("")

for s in site_list:
    get_SSL_Expiry_Date(s, 443)
mailme()
