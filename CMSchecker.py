import requests
import time 

##Check for CMS technology using WhatCMS

url = "https://whatcms.org/API/Tech"

h = {
"Accept-Encoding":"gzip",
"Accept-Language":"fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
}

json_string = ""
myfile = open("fileread.txt", "r")
myline = myfile.readline()

while myline:
    params = {
    "key":"<API KEY>",
    "url": myline
    }

    r = requests.get(url, headers=h, params=params).json()
    time.sleep(10)
    myline = myfile.readline()
    
    json_string = str(json_string) + "\n" + str(r)
    
myfile.close()   

print(json_string)
##print for debug
#print(r)