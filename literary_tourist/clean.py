'''
# Organize data

# For every article
#extract article and title
#now do enetity extractions to double check that it's a bookstore/Library or shop
# for every entity - hit foursquare API and get the address/long/lat
# use webgl in order to create a nice map

'''

import pandas as pd
import requests, json


url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=mykeyhere'
payload = json.load(open("request.json"))
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=json.dumps(payload), headers=headers)

curl -o "literary-tourism-istanbul.html" "https://bookriot.com/2016/04/10/literary-tourism-istanbul/"
gsutil cp "literary-tourism-istanbul.html" gs://literarytourist
gcloud ml language analyze-entities --content-file=gs://literarytourist/literary-tourism-istanbul.html >> literary-tourism-istanbul.json


df = pd.read_csv('data.csv')
for rownum, row in df.iterrows():
	print row


file = 'literary-tourism-istanbul.json'
with open(file) as train_file:
    dict_train = json.load(train_file)

for key, value in dict_train.iteritems():
	print key, value


cleandf = pd.DataFrame(columns= ['entity', 'name', 'type', 'salience'])

for key in dict_train['entities']:
	mention = key['mentions'][0]['text']['content']
	print(mention)
	name = key['name']
	print(name)
	type_ = key['type']
	print(type_)
	salience = key['salience']
	print(salience)
	cleandf.loc[len(cleandf)]=[mention, name, type_, salience]

cleandf.to_csv('literary-tourism-istanbul.csv', index=False, encoding='utf-8')


df = pd.read_json(dict_train)
df = pd.DataFrame([dict_train], columns=dict_train.keys())