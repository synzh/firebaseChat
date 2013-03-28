import subprocess
import json
from time import strftime,localtime
from collections import OrderedDict

""" Get Method """
status = subprocess.check_output(["curl","-s","https://zero99.firebaseio.com/users/jack/name.json"])
print status + "\n"

""" To set formatted time """
xRecTime = strftime("%Y%m%d%H%M%S",localtime())
User_id = raw_input("Your Name is? ")

while True:
   Text_ss = raw_input(User_id + ": ")
   y = "{\"user_id\" : \" " + User_id + " \" , \"text\" :\" " + Text_ss + " \"  , \"time\" : \" "  + xRecTime + " \" }"
   print "y= " + y

   push_data = subprocess.check_output(["curl","-s","-X POST","-d",y,"https://zero99.firebaseio.com/message_list.json"])
   print "pushed: " + push_data + "\n"

   """ Get method to fectch data from firebase """
   status = json.loads(subprocess.check_output(["curl","-s","https://zero99.firebaseio.com/message_list.json"]))
   status = OrderedDict(sorted(status.items(), key=lambda t:t[0]))
   print status

   """ Loop for json format output """
   for FirstKey, FirstValue in status.iteritems():
    # print FirstKey
    #delstatus = subprocess.check_output(["curl","-s","-X DELETE","https://zero99.firebaseio.com/message_list/" + FirstKey + ".json"])
    #print "deleted: " + delstatus 
       temp = ""
       for SecondKey, SecondValue in FirstValue.iteritems():
         #pass
           if SecondKey == "text":
              temp = SecondValue
           if SecondKey == "user_id":
              temp = SecondValue + " says: " + temp
              print temp

   if Text_ss == "close":
      break
