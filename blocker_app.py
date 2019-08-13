
import time
from datetime import datetime as dt # dt is alias for datetime

# hosts file is located at:
# C:\Windows\System32\drivers\etc\hosts  -  windows
# /etc/hosts   -  linux # put this in function 

hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"]

while True:  # if dt.now() or current time is bigger than 8 and less than 16
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("working hours...")
    else:
        print("Fun hours....")
    time.sleep(5)