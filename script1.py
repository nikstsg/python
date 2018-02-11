#!/usr/bin/python

# SCRIPT SEARCHES FOR COMPRESSED (.gz) FILES IN ANY SPECIFIED DIRECTORY, UNCOMPRESSES THE FILES, EXTRACTS IP ADDRESSES, WRITES THEM
# INTO "ip_file" IN THE SAME DIRECTORY WHERE THE SCRIPT IS LOCATED AND SUBSEQUENTLY DELETES ALL UNCOMPRESSED FILES

import re
import os

# REMOVE ip_file IF IT EXISTS
if os.path.isfile("ip_file"):
 os.system("rm ip_file")

# DIRECTORY INPUT
mydir = raw_input("Enter a directory: ")
delete_list = []

# FIND ALL COMPRESSED FILES AND UNCOMPRESS THEM
for root,dirs,files in os.walk(mydir):
 for f in files:
  if f.endswith(".gz"):
   search_f = os.path.join(root,f).split(".gz")[0]
   delete_list.append(search_f) 
   os.system("gzip -d %s" % os.path.join(root,f))

# OPEN AN UNCOMPRESSED FILE AND READ ITS LINES
   f = open(search_f, "r")
   line = f.readlines()

# REGEX TO FIND IP ADDRESSES
   for i in line:
     m = re.findall("(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)", i)

# WRITE IP ADDRESSES INTO "ip_file"
     f2 = open("ip_file", "a")
     for ip in m:
      f2.write("%s\n" % (ip))

# DELETE ALL UNCOMPRESSED FILES
for i in delete_list:
  print "Deleting %s" % i
  os.system("rm %s" % i)
