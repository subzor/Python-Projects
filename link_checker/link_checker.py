import os
import requests

with open("deleted.txt", 'a+') as f:
    for file in os.listdir():
        if file.endswith(".jpg") or file.endswith(".mp4"):
            file1 = file[:-4]
            response = requests.get("https://i.vsco.co/{}".format(file1))
            if response.status_code != 200:
                f.writelines(file+'\n')

