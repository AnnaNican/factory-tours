import pandas as pd
import json, os
import uuid, random
import string 
import datetime, time
import numpy as np

ts = time.time()
today = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%S')

df = pd.read_csv('data_factories.csv')


for rownum, row in df.iterrows():
	# df.loc[rownum, "id"] = str(uuid.uuid1())
	df.loc[rownum, "id"] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
	# df.loc[rownum, "id"] = 'rec0IH8utLHrbSyVW'
	df.loc[rownum, 'Start Date/Time'] = today
	df.loc[rownum, 'End Date/Time'] = today
	df.loc[rownum, 'City'] = 'Test'
	df.loc[rownum, 'createdTime'] = today

# df["id"] = 'rec0IH8utLHrbSyVW'

df.rename(columns={
		'factory_name': 'Name', 
		'description': 'Description',
		'factory_url': 'Website',
		'state': 'State/Province',
		'latitude': 'Latitude',
		'longitude': 'Longitude'}, 
		inplace=True) 

df = df[np.isfinite(df['Longitude'])]


j = (df.groupby(['id', 'createdTime'], as_index=False)
             .apply(lambda x: x[['Name', 'Description', 'Start Date/Time', 'End Date/Time', 'City', 'Website', 'State/Province', 'Latitude', 'Longitude']].to_dict('r'))
             .reset_index()
             .rename(columns={0:'fields'})
             .to_json(orient='records'))



d = json.loads(j)
for numitem, item in enumerate(d):
	print(numitem)
	item['fields'] = item['fields'][0]

e = { "records": d }

with open('data.json', 'w') as outfile:
    json.dump(e, outfile)


# def f(x):
#     return (dict({'factory_name':x.factory_name.iloc[0]},**{k:v for k,v in zip(x.state,x.longitude, x.latitude)}))

# (
# df.groupby(['factory_url','state_url']).apply(f).groupby(level=0).apply(lambda x: x.tolist()).to_dict()
# )




# def write_to_json(fname, entry):
# 	a = []
# 	if not os.path.isfile(fname):
# 	    a.append(entry)
# 	    with open(fname, mode='w') as f:
# 	        f.write(json.dumps(a, indent=2))
# 	else:
# 	    with open(fname) as feedsjson:
# 	        feeds = json.load(feedsjson)
# 	    feeds.append(entry)
# 	    with open(fname, mode='w') as f:
# 	        f.write(json.dumps(feeds, indent=2))

# write_to_json('test.json', j)


# with open('test.json', 'w') as outfile:
#     json.dump(j, outfile)