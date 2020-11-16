import sys
import os
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from function_col import pp, relPath
from app import returnRequest
import pandas as pd
adressse = os.getcwd()+"\\reqbinn"
pp(adressse)

sys.path.insert(0, adressse)
from index import startMyPlot

import plotly
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

from plotly.tools import mpl_to_plotly
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings("ignore",category=plt.cbook.mplDeprecation)

pd.set_option('display.max_columns', 200)
pd.set_option('display.max_rows', 30)
pd.set_option('display.expand_frame_repr', True)

# sys.path.insert(0, os.getcwd())
if os.name=='nt':
	adress = os.getcwd()+"\\DataAfterEditing.csv"
	pp(adress)
elif os.name=='posix':
	adress = os.getcwd()+"/DataAfterEditing.csv"
	pp(adress)
# sys.path.insert(0, adress)

df = pd.read_csv(adress)
# raise Exception
df.drop('Unnamed: 0', axis=1, inplace=True)

from threading import Thread
from time import sleep

dici = df[df.columns.values].iloc[[0]].to_dict()
df2 = pd.DataFrame(dici, index=[0])
df = df.iloc[[0]]
df = df.append(df2, ignore_index=True)
port_api = 5000

app = Flask(__name__)
api = Api(app)

# The proper way to never forget how decorators work is just keeping in mind what that '@' syntax means: 

# @decorator
#  def function():
#     ...

# is equivalent to: function = decorator(function).



def updatePeriod():
	sleep(20)
	for i in range(2):
		updatePlotNow(i*10)
		sleep(5)


# application._insert_callback(updatePeriod(inputs='figure', state=))

#-------------------------------------------------------------------------------






def startMyApi():
	# global df, abst, indexx, dfPost, returnRequest, app


	# returnRequest.initializeDfIndexAbst(returnRequest, df, indexx, abst)
	returnRequest.df = df
	# returnRequest.updatePlot = updatePlot

	# @returnRequest.updatePlot()
	# def updatePlot(n=10):
	# 	fig= plt.figure()
	# 	ax= fig.add_subplot(111)
	# 	ax.plot(range(10), [i**2 for i in range(n)])
	# 	ax.grid(True)
	# 	plotly_fig = mpl_to_plotly(fig)
	api.add_resource(returnRequest, "/request")	
	# tPost.start()
	app.run(debug=False, host = '0.0.0.0', port=port_api)
	# raise Exception



if __name__ == '__main__':


	tApi = Thread(target=startMyApi)
	# tPlot = Thread(target=startMyPlot)
	# tPost = Thread(target=postFunction, args=(dfPost,))
	# tPost = Thread(target=postFunction)
	# tdfPrint = Thread(target=printDf)
	

	# tPlot.start()

	# tUpdate = Thread(target= updatePeriod)
	# tUpdate.start()

	# tPost.start()
	pp("starting api...")
	tApi.start()
	
	startMyPlot()


	# startMyApi()
	# sleep(10)
	# pp("starting plot")
	# startMyPlot()
