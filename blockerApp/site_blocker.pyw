import time
from datetime import datetime as dt

host_temp=r"C:\Users\sai kiran pothula\PycharmProjects\Exercises\venv\hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
site_list=["www.facebook.com", "facebook.com", "www.twitter.com", "twitter.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print("Working Hours....")
        with open(host_temp, "r+") as file:
            content=file.read()
            for site in site_list:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+ site+"\n")
    else:
        print("Fun Hours.....")
        with open(host_temp, "r+") as file:
            content=file.readlines()
            file.seek(0)
            file.truncate()
            for line in content:
                if not any(site in line for site in site_list):
                    file.write(line)
#            file.truncate()
    time.sleep(5)
