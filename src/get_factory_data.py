
import requests
from bs4 import BeautifulSoup
import pandas as pd



def find_states():
	page = requests.get('http://www.factorytoursusa.com/')
	soup = BeautifulSoup(page.text, 'html.parser')


	states = soup.find_all('a')


	data = pd.DataFrame(columns=[])
	# create 

	data['html'] = states

	for rownum, row in data.iterrows():
		url = re.findall(r'href="(.*)">', str(row['html']))[0]
		if 'state' not in url:
				next
		else:
			data.loc[rownum, 'state'] = re.findall(r'>(.*)<', str(row['html']))[0]
			data.loc[rownum, 'url'] = re.findall(r'href="(.*)">', str(row['html']))[0]

	data.dropna(subset=['state'], inplace=True)

	return states


def get_factories_from_state(state_url):
	factory_df = pd.DataFrame(columns=[])
	page = requests.get(state_url)
	soup = BeautifulSoup(page.text, 'html.parser')
	factories = soup.find_all('tr')
	for n, factory in enumerate(factories):
		factory_url = re.findall(r'href="(.*)">', str(factory))[1]
		print(factory_url)
		factory_name = re.findall(r'href="(.*)">(.*)<\/a>', str(factory))[0][1]
		print(factory_name)
		factory_df.loc[n, 'factory_name'] = factory_name
		factory_df.loc[n, 'factory_url'] = str('http://www.factorytoursusa.com' + factory_url)
	return factory_df



def get_factory_details(factory_url):
	# global df
	# df = pd.DataFrame(columns=['factory_name', 'longitude', 'latitutde', 'description', 'hours', 'factory_meta', 'factory_url'])
	# df.loc[0, 'factory_url'] = url
	# page = requests.get('http://www.factorytoursusa.com/state/alabama/blue-bell-creameries-sylacauga-al/')
	# page = requests.get('http://www.factorytoursusa.com/state/alabama/buds-best-cookies/')\
	page = requests.get(factory_url)
	soup = BeautifulSoup(page.text, 'html.parser')
	#
	soup.find_all(text=re.compile('Longitude:(.*)<'))
	longitude_str = str((soup(text=re.compile('Longitude'))))
	longitude = re.findall(r'Longitude: (.*)\'\]', longitude_str)[0]
	latitude_str = str((soup(text=re.compile('Latitude'))))
	latitude = re.findall(r'Latitude: (.*) \\', latitude_str)[0]
	# df.loc[0, 'longitude'] = longitude
	# df.loc[0, 'latitude'] = latitude
	#
	meta_data = soup.find_all(class_='row-fluid')
	for meta in meta_data:
		if '<u><b>Company</b></u><br/>' in str(meta):
			company_meta= str(meta).replace('\n', ' ').replace('\r', '')
			company_meta = re.sub(' +', ' ', company_meta)
			df.loc[0, 'factory_meta'] = company_meta
			# company = re.findall(r'<b><u>Company<\/u><\/b><br\/\>(.*)<\/div>', company_meta)
			# print(company)
		elif '<u>Hours</u>' in str(meta):
			# meta_h = meta
			hours_meta= str(meta).replace('\n', ' ').replace('\r', '')
			hours_meta = re.sub(' +', ' ', hours_meta)
			hours = re.findall(r'<b><u>Hours<\/u><\/b><br\/\>(.*)<\/div>', hours_meta)
			# df.loc[0, 'hours'] = hours
			# print(hours)
		elif '<u>Description</u>' in str(meta):
			# meta_h = meta
			description_meta= str(meta).replace('\n', ' ').replace('\r', '')
			description_meta = re.sub(' +', ' ', description_meta)
			description = re.findall(r'<b><u>Description<\/u><\/b><br\/\>(.*)<\/div>', description_meta)
			# df.loc[0, 'description'] = description
			# print(description)
		else:
			next
	return longitude, latitude, hours, description, meta_data




# get_factory_details('http://www.factorytoursusa.com/state/alabama/tiffin-motorhomes/')

# for meta in meta_data:
# 	print(meta)
# 	if '<u>Company</u>' in str(meta):
# 		print(meta)
# 	else:
# 		print('not this')










# first get all states
find_states()
# get all factories per state
data_factories = pd.DataFrame(columns=['factory_name', 'factory_url'])
for rownum, row in data.iterrows():
	stateurl = str('http://www.factorytoursusa.com'+ row['url'])
	factory_df = get_factories_from_state(stateurl)
	factory_df['state'] = row['state']
	factory_df['state_url'] = row['url']
	data_factories = data_factories.append(factory_df)
# reset indec


# loop through all factories and get their metadata
newcols = ['longitude', 'latitutde', 'description', 'hours', 'factory_meta']
data_factories.reindex([*data_factories.columns, *newcols], axis=1)

# pd.concat([df,pd.DataFrame(columns=list('longitudelatitutde', 'description', 'hours', 'factory_meta'))])
# data_factories.reindex(columns=list('longitude', 'latitutde', 'description', 'hours', 'factory_meta'))
for rownum, row in data_factories.iterrows():
	print(row['factory_url'])
	factory_details = get_factory_details(row['factory_url'])
	data_factories.loc[rownum, 'longitude'] = str(factory_details[0])
	data_factories.loc[rownum, 'latitude'] = factory_details[1]
	data_factories.loc[rownum, 'hour'] = factory_details[2]
	data_factories.loc[rownum, 'description'] = factory_details[3]
	data_factories.loc[rownum, 'metadata'] = str(factory_details[4])

data_factories.to_csv('data_factories.csv', index=False)








# b_el = meta_h.find('b',text='Hours')
# b_el.next_sibling.next_sibling.next_sibling.next_sibling     # contains " Test title"


# # this is actually works and neat way to do
# for i in len(meta_h.contents)
# 	while meta_h.contents[i] not in ['\\n', , 3]:
# 		hours = meta_h.contents[i]
# # The Loop 1

# # for every state, get all the factory names -> store in the table

# # Now iterate through second tab;le
# #for every factory, create the url, pull the file and then get_factrory_details

# if 'Company' in str(meta_data[3]):
# 	print('yes')
# else:
# 	print('no')
