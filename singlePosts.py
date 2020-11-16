import requests
import pickle
import base64
import pandas as pd
from random import randint
from function_col import pp, relPath
import sys
from time import sleep

class postIt():
	# def __init__(self, dfPostForThread):
	# 	self.dfPost = dfPostForThread
	# 	# self.dfPostt = self.dfPost 

		
	def postDataNow(self, index_ex):
		index = index_ex
		pd.set_option('display.max_columns', 200)
		pd.set_option('display.max_rows', 30)

		pd.set_option('display.expand_frame_repr', True)
		df = pd.read_csv("C:/Users/nicol/Desktop/python/sicherheitkopie/PressurePrediction/DataAfterEditing.csv")
		df.reset_index(drop=True, inplace = True)

		dici = df[df.columns.values].iloc[[6]].to_dict()
		df2 = pd.DataFrame(dici, index=[0])
		df.drop('Unnamed: 0', inplace=True, axis=1)
		df = df.iloc[[index]]
		self.dfPost = df.copy()
		pp(self.dfPost)
		base = "http://127.0.0.1:5000/request"
		indexList = self.dfPost.index.to_list()

		index = indexList.pop(0)
		indexList = self.dfPost.index.to_list()
	
		# sleep(20)
		# for i in range(6):
		# x = randint(40, 60)

		x = 5
		df_dummy = self.dfPost[self.dfPost.columns.values]
		# df_dummy.to_csv('self.dfPostedToFlask'+str(index)+'.csv', index=False)

		dff = self.dfPost[self.dfPost.columns.values].to_dict()
		# pp(dff)
		pickled = pickle.dumps(dff)
		# pp(pickled)
		pickled_b64 = base64.b64encode(pickled)
		# pp(pickled_b64)
		pickled_b64	

		
		response = requests.post(base, data =pickled_b64)
		index = indexList.pop(0)
		# sleep(x)
		# if i==5:
				# raise Exception



p = postIt()
for i in range(29):
	p.postDataNow(5+i)
	sleep(10)

