#!/usr/bin/python
import argparse
import ssl
import socket
import datetime
import sys
import json

parser = argparse.ArgumentParser(description='Check if SSL cert needs to be updated, either expired, or will expire in a day')
parser.add_argument('hostname', help='hostname to check')
args = parser.parse_args()
hostname = args.hostname
ctx = ssl.create_default_context()
s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
try:
    s.settimeout(15)
    s.connect((hostname, 443))
    cert = s.getpeercert()
    expire = cert["notAfter"]
    issuer = cert["issuer"]
    for x in issuer:
        if 'commonName' in dict(x):
            commonName = dict(x)['commonName']
    today = datetime.datetime.today()
    format = "%b %d %H:%M:%S %Y %Z"   
    expire_date = datetime.datetime.strptime(expire, format)
    delta = expire_date - today
    if commonName:
        print "Issuer: %s" % commonName
    print "Today: %s" % today
    print "Expires: %s" % expire_date
    print "Days Left: %s" % delta.days
    if delta.days <= 1:
        print "Cert needs update"
        sys.exit(1)
    else:
        sys.exit(0)
except ssl.SSLError, e:
    print e
    print "Cert needs update"
    sys.exit(1)
except socket.gaierror, e:
    print "Unable to grab cert"
    print e
    sys.exit(2)
except Exception, e:
    print "I did not code for this error"
    print e
    print type(e)
    sys.exit(2)
