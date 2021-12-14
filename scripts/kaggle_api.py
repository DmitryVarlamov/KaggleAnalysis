from datetime import datetime
import time

import kaggle
import json
import requests
import logging

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()



i=1
start_time = datetime.now()
try:
    while(True):
        if api.competitions_list_with_http_info(page=i)[0] == []:
            break
        print(f"Trying to get page {i}")
        page_info = api.competitions_list_with_http_info(page=i)[0]
        for x in page_info:
            x["kaggle_type"] = 'competition'
            try:
                requests.post(url="http://167.99.143.159:5045", json=x)
            except Exception:
                time.sleep(5)
                requests.post(url="http://167.99.143.159:5045", json=x)
        i = i + 1
except Exception as e:
    print(e)
    pass

end_time = datetime.now()
duration = end_time -  start_time
print("Downloading and importing competitions took")
print(duration)

start_time = datetime.now()
i=1
try:
    while(True):
        if api.datasets_list(page=i) == []:
            break
        print(f"Trying to get page {i}")
        page_info = api.datasets_list(page=i)
        for x in page_info:
            x["kaggle_type"] = 'dataset'
            try:
                requests.post(url="http://167.99.143.159:5045", json=x)
            except Exception:
                time.sleep(5)
                requests.post(url="http://167.99.143.159:5045", json=x)
        i = i+1
except Exception as e:
    print(e)
    pass

end_time = datetime.now()
duration = end_time -  start_time
print("Downloading and importing datasets took")
print(duration)
