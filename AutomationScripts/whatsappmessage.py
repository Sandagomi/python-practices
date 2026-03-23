import pywhatkit as kit
from datetime import datetime


number = input("enter number with country code: ")
message = input("enter message: ")


#most important - setting the time

now = datetime.now()
hour = now.hour
minute = now.minute + 2

#the reason for  + 2 is
#I want to keep a gap of 2 mins
#once i run the script msg will send after 2 mins

if minute >= 60:
    hour += 1
    minute = minute % 60

#sending the message
print("sending the message...")
kit.sendwhatmsg(number, message, hour, minute)

print("message sent successfully!")

