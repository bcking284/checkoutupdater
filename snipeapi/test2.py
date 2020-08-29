import json

with open('test.json') as asset_file:
    data = json.load(asset_file)
    count=0
    for p in data['rows']:
        print(p['id'])
        count +=1

print(count)
