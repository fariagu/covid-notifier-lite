import time
import requests
from fastapi.encoders import jsonable_encoder


while True:
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
    response = requests.get("http://localhost:8000/covid/list")

    if response.status_code == 200:
        print(response.content)

    time.sleep(300)
