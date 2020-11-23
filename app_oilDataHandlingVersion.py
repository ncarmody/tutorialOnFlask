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

	def post(self):
		
		if self.df.shape[0]>1:
			try:
				self.df = pd.read_csv('file.csv')
			except:
				print('stop')
				pass

		pickled_b64 = request.get_data(as_text=False)
		dataFordf = pickled_b64.decode('utf-8')

		dictlist = pickle.loads(base64.b64decode(dataFordf.encode()))
		print('huerePingu')
		pp(dictlist, sc='dictlist')
		df_dictlist = pd.DataFrame(dictlist, columns=self.df.columns)

		if self.df.shape[0]>0:

			self.df = self.df.append([df_dictlist], ignore_index=True)

		else:
			self.df = df_dictlist
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
