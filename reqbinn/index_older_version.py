# Solution to Challenge.
# Changes made to line 41

import pandas as pd
import plotly
import plotly.express as px
import sys
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from requestBin import getData
from function_col import pp, relPath
# sys.path.insert(0, 'C:/Users/nicol/Desktop/python/tutorialOnFlask')
from plotly.tools import mpl_to_plotly
from matplotlib import pyplot as plt
import warnings
import os
warnings.filterwarnings("ignore",category=plt.cbook.mplDeprecation)



port = 8050
# from alpha_vantage.timeseries import TimeSeries

# key = '7FEDJMHY3CM2KPEC'
# ts = TimeSeries(key, output_format='pandas')

#-------------------------------------------------------------------------------
# Building our Web app and update financial data automatically
# address = '\\'.join(os.getcwd().split('\\')[:-1])+"\\file.csv"
if os.name=='nt':
    address = os.getcwd()+"\\file.csv"
    # address.
    pp(address)
elif os.name=='posix':
    address = os.getcwd()+"/file.csv"
    # address.
    pp(address)


application = dash.Dash(__name__)

application.layout = html.Div([
    dcc.Interval(
                id='my_interval',
                n_intervals=0,       # number of times the interval was activated
                interval=1*1000,   # update every 2 minutes
    ),
    dcc.Graph(id="world_finance"),   # empty graph to be populated by line chart
])



#-------------------------------------------------------------------------------
@application.callback(
    Output(component_id='world_finance', component_property='figure'),
    [Input(component_id='my_interval', component_property='n_intervals')]
)
def update_graph(n):


    df = pd.read_csv(address)
    
    line_chart = px.line(

                    data_frame=df,
                    x=df.columns.values[0],
                    y=df.columns.values[3],
                    # color='indicator',
                    title="Stock: "
                 )
    
    return (line_chart)




#-------------------------------------------------------------------------------
def startMyPlot():

    application.run_server(debug=False, host='0.0.0.0',port=port)

# if __name__ == '__main__':
    # application.run_server(debug=True,port=port)
# startMyPlot()
# def update_graph(n):
#     df = pd.read_csv("C:/Users/nicol/Desktop/python/tutorialOnFlask/file.csv")
#     new = df.shape[0]
#     fig= plt.figure()
#     ax= fig.add_subplot(111)
#     ax.plot(range(new), [i**2 for i in range(new)])
#     ax.grid(True)
#     plotly_fig = mpl_to_plotly(fig)
#     return plotly_fig