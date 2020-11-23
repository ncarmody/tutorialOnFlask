# "AA0WAAlCABwWAAt3AAlgABXg"
from flask import Flask, request
from flask_restful import Api, Resource, reqparse

import base64
import requests
import pickle
import base64
import pandas as pd
from random import randint
from function_col import pp, relPath
import sys
from time import sleep
from function_col import pp, relPath
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import sys
import pandas as pd
import os

# df = pd.read_csv("C:/Users/nicol/Desktop/python/sicherheitkopie/PressurePrediction/DataAfterEditing.csv")
# listt = self.df.index.to_list()
# index = listt.pop(0)
# df = df[self.df.columns.values].iloc[[index]]
# pp(df)
# pp(type(df))
# raise Exception







# db = SQLAlchemy(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# engine = create_engine('sqlite:///test.db')
# db.create_all()



if sys.argv.__len__() > 1:
	port = sys.argv[1]

	pp(port)
# pp(port)
# https://blog.restcase.com/restful-api-authentication-basics/
# https://www.w3resource.com/pandas/dataframe/dataframe-to_sql.php
# http://51.103.157.153:5000/request
# sensorData = reqparse.RequestParser()
# dictOfKeys = [["data", bytes]]
# [sensorData.add_argument(i[0], type=i[1], help = str(i[0])+" is missing", required = True) for i in dictOfKeys]
# api.add_resource(returnRequest, "/request")

# class sensorModel(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	pandasDataframe=  db.Column(db.Integer)




class returnRequest(Resource):
	# def updatePlot(self):
	# 	pass
		
	def get(self):
		return {"data":"hello world"}

	def rshift(self, val, n): return (val % 0x100000000) >> n

	def PayloadDecoder(self, fullJson):
		toBeDecoded = fullJson['data']
		# v = {"cmd":"gw","seqno":103915,"EUI":"FFFFFFFFFFFFFFFA","ts":1606054046489,"fcnt":2,"port":1,"freq":868500000,"toa":56,"dr":"SF7 BW125 4/5","ack":false,"gws":[{"rssi":-71,"snr":10,"ts":1606054046489,"tmms":null,"time":"2020-11-22T14:07:26.485739Z","gweui":"647FDAFFFF007AFB","ant":0,"lat":47.40912537932723,"lon":8.549648523330688}],"sessionKeyId":null,"bat":255,"data":"01bbd70009d80010"}
		# v = request.get_jason()
		# v = v['data']

		# toBeDecoded = bytearray.fromhex("01a93b0009e20010")
		# toBeDecoded = bytearray.fromhex(toBeDecoded['data'])
		# toBeDecoded = bytearray.fromhex("01bbd70009d80010")
		toBeDecoded = bytearray.fromhex(toBeDecoded)
		# toBeDecoded = 0x01bbd70009d80010
		pp(toBeDecoded)
		# for b in toBeDecoded:
			# print(b)
		i = 0
		dataDict = {'distance':0.0, 'temperature': 0.0,'humidity': 0.0, 'time': "", 'year': None, 'month': None, 'day': None, 'date': None}

		dataDict['distance'] = (self.rshift((toBeDecoded[i]<<16),0) + self.rshift((toBeDecoded[i+1]<<8),0) + toBeDecoded[i+2])/100
		
		# pp(dd)
		i += 3
		dataDict['temperature'] = (self.rshift((toBeDecoded[i]<<16),0) + self.rshift((toBeDecoded[i+1]<<8), 0) + toBeDecoded[i+2])/100
		# pp(dd)
		i += 3
		dataDict['humidity'] = (self.rshift((toBeDecoded[i]<<16), 0) + self.rshift((toBeDecoded[i+1]<<8), 0))/100
		dataDict['time'] = pd.to_datetime(fullJson['gws'][0]['time'], infer_datetime_format=True)
		dataDict['date'] = pd.to_datetime(fullJson['gws'][0]['time'], infer_datetime_format=True).date
		dataDict['year'] = pd.to_datetime(fullJson['gws'][0]['time'], infer_datetime_format=True).year
		dataDict['month'] = pd.to_datetime(fullJson['gws'][0]['time'], infer_datetime_format=True).month
		dataDict['day'] = pd.to_datetime(fullJson['gws'][0]['time'], infer_datetime_format=True).day

		return [dataDict, list(dataDict.keys())]

		# pp(dd)
		


	def post(self):
		
		if self.df.shape[0]>1:
			try:
				self.df = pd.read_csv('file.csv')
				os.system('echo: '+str(self.df)+ ' IN START OF POST')
				pp(self.df, sc=' VON CSV ')
				# self.df['time'] = pd.to_datetime(self.df[['time']])
				# self.df.set_index('time', inplace=True)
			except:
				print('no file there so far')
				pass
		# pickled_b64 = request.get_data(as_text=False)
		# request.get_data()

		pickled_b64 = request.get_json()
		os.system('echo: '+str(pickled_b64))
		# sys.
		# dff = pd.DataFrame(pickled_b64, columns = list(pickled_b64.keys()))
		# dff.to_csv('debug.csv', index=False)

		pp(pickled_b64, sc='pickled_b64')

		# pickled_b64 = self.PayloadDecoder(pickled_b64)

		# dataFordf = pickled_b64.decode('utf-8')
		dictToSave, columns = self.PayloadDecoder(pickled_b64)
		pp(dictToSave)
		pp(columns)

		# dictlist = pickle.loads(base64.b64decode(dataFordf.encode()))
		print('huerePingu')
		# pp(dictlist, sc='dictlist')
		df_dictlist = pd.DataFrame(dictToSave, index = [self.df.shape[0]+1])
		# df_dictlist = pd.DataFrame(dictlist, columns=self.df.columns)
		os.system('echo: '+str(self.df))
		os.system('echo: '+str(df_dictlist))


		if not self.df.empty:
			# self.df = self.df.append
			self.df = self.df.append(df_dictlist)

			os.system('echo: '+str(self.df)+' this is if')
		else:
			self.df = df_dictlist
			os.system('echo: '+str(self.df)+' this is else')

		# pp(self.indexx)
		# df = self.df.append(dff, ignore_index=True)
		# df = pd.read_json(request.get_json())
		# df = pd.DataFrame.from_dict(request.get_json(),columns=['device_id', 'distance1', 'humidity1'])
		# args = sensorData.parse_args()
		# df = pd.DataFrame(args)
		# falls database voll oder allg.
		
		# self.df.to_sql(name='test', con=engine, index=True, if_exist='append')
		# df = pd.read_sql_table("test", engine)
		# print({"data is": args})

		print(self.df)

		self.df.to_csv('file.csv', index=False)
		# self.df.to_csv('dfAtEnd'+str(self.df.shape[0])+'.csv', index=False)
		return 'ok'


# # @returnRequest.updatePlot
# def updatePlot(n=10):
# 	# fig= plt.figure()
# 	# ax= fig.add_subplot(111)
# 	# ax.plot(range(10), [i**2 for i in range(n)])
# 	# ax.grid(True)
# 	# plotly_fig = mpl_to_plotly(fig)
# 	print('blabla')
# returnRequest.updatePlot = updatePlot
