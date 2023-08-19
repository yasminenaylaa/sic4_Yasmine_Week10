import time
import requests
import math
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()
suhu = sensor.get_temperature()
fahrenheit = W1ThermSensor

TOKEN = "BBFF-xkYsIgR7S6pzMasA15S5PFTMohj8cL"  
DEVICE_LABEL = "demo"   
VARIABLE_LABEL_1 = "demo"  
VARIABLE_LABEL_2 = "new-variable"  
VARIABLE_LABEL_3 = "position"  


def build_payload(variable_1, variable_2, variable_3):
    # Creates two random values for sending data
    value_1 = suhu

    payload = {variable_1: value_1,
               #variable_2: value_2,
               #variable_3: {"value": 1, "context": {"lat": lat, "lng": lng}}
               }
    return payload


def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True


def main():
    payload = build_payload(
        VARIABLE_LABEL_1, VARIABLE_LABEL_2, VARIABLE_LABEL_3)

    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")


if __name__ == '__main__':
    while (True):
        main()
        time.sleep(1)
