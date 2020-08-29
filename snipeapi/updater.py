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
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjBjN2E2ZTY4OTA4MDUxMjFhNTdmZmZkMWVjNjNiYjExOGE5ZTJkYzViYTFkYWYzYzkxOGIwODIwOGRhNDFkOTZlZGQ5Y2I2MTgwOTM4NjMzIn0.eyJhdWQiOiIxIiwianRpIjoiMGM3YTZlNjg5MDgwNTEyMWE1N2ZmZmQxZWM2M2JiMTE4YTllMmRjNWJhMWRhZjNjOTE4YjA4MjA4ZGE0MWQ5NmVkZDljYjYxODA5Mzg2MzMiLCJpYXQiOjE1OTc5MzMxNTYsIm5iZiI6MTU5NzkzMzE1NiwiZXhwIjoxNjI5NDY5MTU2LCJzdWIiOiIzNCIsInNjb3BlcyI6W119.YCxJnQXOGeEFo5yv0XAo5oJMMEWW74so-JG9OLRfcNcp6JOCsBf_s1rv9XDNGYPQZgBNT6Xn3lI2IwOs4n42jEYmALX8lcWaMxhZXFVGQoSwZHebHka3aJnV2C784oC4-L2m_0jMmP065wfczDRHCP3rL6MVmOjcEhW28s0i72BuJmQUP4_2yBpj3--Lr9HsvnEF0hiBZAm1ap9Cayzfj8EyyMKtaMb2KBWkUTY-VSOMTPnB98wGb3eP7J3o-1plFvye1_MGc3TeEkga3CuQBgu3hRs7YaA3XY-51lybd78Rdp6QmeLEM3YldhI2O_ySG6ViChfF3wGt53vyxfwdcVYzrJk1aAJMTt8pxm6NXJmAxnJNHfNAVl6PDc2XMtAJnJ9UDl-cwNWK6Cyql7TEpzNlAtmWiRrioIhWoOc7UBB-jaeqJT99i7KPJWoqLXAq5Pel2sVWaDkd0Q7apyuQYde3Yq4AwOiON1oiYZmmIsdxWFfiMy8HU7-ycwvw6C1XhtO39nHBzqeIGcXJwLRy77ABt8_Ebzzai89amXfp47cnNJJNTZzPCcB2E1DQweJCTd7i5t_uv_8bJfFVpJEpA6Z19XI69VwLK6tMsXrndw1t0QO_JYxf7IrAwN-Yl7lZd-q1yCO6atjm4gZyczrvNsIAq0pXHdEEK_BwsxJIta4',
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
