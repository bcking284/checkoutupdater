import requests
import json
import pandas as pd
import numpy as np
import csv
from datetime import datetime
import time


url = "http://snipeit.birmingham.dom/api/v1/hardware"
payload = {}
files = {}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <API key>',
  'Cookie': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImJiNjFiMjBlYTRhMjZhYTM3NzdlNGI4ZjBjYzlkYTllYmU2Yjc5N2JmYzYwNjRkMGEyZjRhN2Q5NWQyZTU0OGZmNTg3ZjM0MzFkY2FlYTA5In0.eyJhdWQiOiIxIiwianRpIjoiYmI2MWIyMGVhNGEyNmFhMzc3N2U0YjhmMGNjOWRhOWViZTZiNzk3YmZjNjA2NGQwYTJmNGE3ZDk1ZDJlNTQ4ZmY1ODdmMzQzMWRjYWVhMDkiLCJpYXQiOjE1OTg0Nzg1MTQsIm5iZiI6MTU5ODQ3ODUxNCwiZXhwIjoxNjMwMDE0NTE0LCJzdWIiOiIzNCIsInNjb3BlcyI6W119.GQYorrry28gH0qQs05ISYeNgl_CtxLdT14EeZqAL7ma1blczWq-Gw-MhG3E0bt92um7rLEdnjQl4sKGxrAKn91vdmNrSen4saM1CKj8P23C8roak506lsbSE2-jxSYEryVeknAb33IIO4nvVypTqLZZ5S32gXR-QndheOBQHOynAzIgOJdO-97qPsIDHOEfPCQInCTCUPJSckJTBMIGPsi5MqOXa9fUlkIjTZXVsbKPO8yiCaW53-Rn-JS1My1yaKpqT9gOMRHY9v2BT1rNISHNjBCRhbM5Qiq55Mo99zhd-55aBtU8cO2549H8-VfLdJIHTqRWXQyxxzkrdxRL3PbpwVwLttu1zLfw7YIk1rBJa0XQC3v2-Q88K0YMxdYtEIKdvWC2d73XACclaUR4fnIYkIeBRGAjd39GXfxiM0Nbc8QZFEVe6ek5Fb11yRFy-4MmZWX10fKFInIt7tgLvROVpK3N38uzlyFJRXepCs418aWLyrynpxxqWyft9F5WmL20h4o_UhZGqhhruX_OuX8SkTi8Q1gxGoHwuOVFsnsCHDMyUxbFyZ6IK_m1YsCn05OWe8vCngqS_RsEbgXoTH3qKzaWvBqvyuK1MQYgiQzzoCtmQGWNHxcuEtRc_nAJmqA4o7k6Olhbc5NpBxjxTlxaalat7HpBA_2fOsEZgIt4'
}

response = requests.request("GET", url, headers=headers, data = payload, files = files)
data = (response.json())

snipedf = pd.json_normalize(data['rows'])
dcidf = pd.read_csv("Desktop Computer Inventory.csv")

mergeddf = pd.merge(left=dcidf, right=snipedf, left_on='SerialNumber', right_on="serial")





for index, row in mergeddf.iterrows():

    snipeuser = mergeddf['assigned_to.username']
    dciuser = mergeddf['UserName']
    date_last_login = datetime.strptime(mergeddf['RunDate'], "%m/%d/%Y %H:%M:%S")
    timedelta = datetime.now() - date_last_login


    if snipeuser != dciuser and timedelta.days < 2:

        userid = mergeddf['assigned_to.id']
        hardwareid = mergeddf['id']
        checkinurl = f"http://snipeit.birmingham.dom/api/v1/hardware/{hardwareid}/checkin"
        checkinpayload = {"note": f"didn't matech in desktop computer inventory report, checking out to last logged in user {dciuser}"}

        response = requests.request("POST", checkinurl, json=checkinpayload, headers=headers)

        print(response.text)


        checkouturl = f"http://snipeit.birmingham.dom/api/v1/hardware/{hardwareid}/checkout"
        checkoutpayload = {
            "checkout_to_type": "user",
            "assigned_user": f"{userid}"
        }


        response = requests.request("POST", checkouturl, json=checkoutpayload, headers=headers)

        print(response.text)

    time.sleep(500)
