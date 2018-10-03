#!/usr/bin/python
# By Nik

import re
import socket
import urllib2
from xml.dom import minidom
import json

temp = {'servers': []}
f = open('/root/ilo/hosts','r')
for line in f:
 if line.startswith("#CHILDREN"):
  break
 else:
  if not line.startswith("#") and not line.startswith('[') and not re.match(r'^s*$', line):
   content = line.strip().partition(' ')[0]
 
   print content
   addr = socket.gethostbyname(content)

   url = "https://%s-ilo/xmldata?item=All" % content
   print url
   page = urllib2.Request(url)
   doc = minidom.parse(urllib2.urlopen(page))
   name = doc.getElementsByTagName("FWRI")[0]
   name2 = doc.getElementsByTagName("PN")[0]
   name3 = doc.getElementsByTagName("SPN")[0]
   name4 = doc.getElementsByTagName("SBSN")[0]

   dict = {'ILO IPv4': addr, 'sn' : name4.firstChild.data, 'name' : content, 'fwri' : name.firstChild.data, 'version' : name2.firstChild.data, 'hwr' : name3.firstChild.data}
   [temp['servers'].append(dict)]

with open("hp.json", "w") as outfile:
 json.dump(temp,outfile,indent=3,sort_keys=False)

