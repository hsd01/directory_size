__author__ = "HemantDhanwar"
__email__="HemantDhanwar@lucidmotors.com"
#"Sathya Madhu" <SathyaMadhu@lucidmotors.com>
import EmailServices as es

T_size = 200
# disk_usage("target drive","output where to save csv")
es.disk_usage('C:/','D:/')

# get_directory_size("Target drive")
size = es.get_directory_size("C:/") # this function will calculate drive size
gb = (size/pow(2,20))/1024
#email_with_attachhment("sender's mail","sender's mail secret key", "reciever1, reciever2,reciever3", "path where csv file is saved")
#es.email_with_attachhment('HemantDhanwar@lucidmotors.com', 'D:\\H_Work_SPACE\\key.txt', 'HemantDhanwar@lucidmotors.com', 'D:\\')

print("Size:", size)
if T_size < gb:
    print("Space is running out")
    print("notifing people in organisation")
    es.email_with_attachhment('HemantDhanwar@lucidmotors.com', 'D:\\H_Work_SPACE\\key.txt', 'HemantDhanwar@lucidmotors.com,SathyaMadhu@lucidmotors.com', 'D:\\')
else:
    print("space is good to go")

# 1 Tb limit 900 
