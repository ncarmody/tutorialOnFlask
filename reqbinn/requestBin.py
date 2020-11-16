
import json
import pandas as pd
# import matplotlib.pyplot as plt
# r = requests.get('https://ttgo_tbeam_deepsleep.data.thethingsnetwork.org/api/v2/query')
import sys
# sys.path.insert(0, "C:/Users/nicol/PycharmProjects/ewz/function_col")
# importing the requests library 
import requests

# from function_col import pp
# api-endpoint 

def getData():
	URL = 'https://ttgo_tbeam_deepsleep.data.thethingsnetwork.org/api/v2/query'

	#which time perios do you want the data to be ? (2d,1h,30s)
	timeElement = "?last=15d"

	URL = URL+timeElement

	# location given here 
	key = 'ttn-account-v2.XT3wGw_6rK3_WGWi0JicWe3lVwPahL-LXcet7ZAHWnY'
	  
	# defining a params dict for the parameters to be sent to the API 
	# PARAMS = {'key': key} 
	headers = {'Accept': 'application/json','Authorization': 'key ttn-account-v2.XT3wGw_6rK3_WGWi0JicWe3lVwPahL-LXcet7ZAHWnY'}


	# sending get request and saving the response as response object 
	r = requests.get(url = URL, headers = headers)


	  
	# print(r)
	# extracting data in json format 
	data = r.json()
	df = pd.DataFrame(data)
	# pp(df)
	# pp(df.columns)
	# pp(df.columns.values[[1,2,3,4]])
	df.drop(df.columns.values[[1,2,3,5,6]], axis=1, inplace=True)
	# pp(type(df['time'])) 
	df['time'] = pd.to_datetime(df['time' ])
	# pp(df[['altitude', 'time']])
	# df[['altitude']].plot()
	# plt.show()
	# pp(type(df['time'])) 


	# pp(df)
	return df
# dff = df.d

# df = pd.DataFrame(data)

# print(da ta)
# dff = getData()
# print(dff)