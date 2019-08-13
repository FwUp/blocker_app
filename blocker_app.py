
import time
from datetime import datetime as dt # dt is alias for datetime

# hosts file is located at:
# C:\Windows\System32\drivers\etc\hosts  -  windows
# /etc/hosts
# write a function to check operating system
# change file name from .py to .pyw in windows to work in background
# use task scheduler in windows to run schedule when should app work
# check "run with highest privileges" to run app as admin

# use cron on linux to schedule app 
# sudo crontab -e
# @reboot python3 /home/aca/Desktop/blocker_app/blocker_app.py
# start app when computer is rebooted

hosts_path = "/etc/hosts"
hosts_temp = "hosts"   # temporary hosts file used for experimenting
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"]

while True:  # if dt.now() or current time is bigger than 8 and less than 16
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("working hours...")
        with open(hosts_path, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content: # if item in hosts do nothing
                    pass               # else write it to hosts file
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0) # set pointer at beggining of file
            for line in content: # if not any item in line for item in website_list
                if not any(website in line for website in website_list):
                    file.write(line) # write all lines except those who have items from website_list
            file.truncate() # delete everything after this line in file
        print("Fun hours....")
    time.sleep(5)
    
    