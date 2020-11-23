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
from application import application
from requestBin import getData
from function_col import pp, relPath
# sys.path.insert(0, 'C:/Users/nicol/Desktop/python/tutorialOnFlask')
from plotly.tools import mpl_to_plotly
import chart_studio.plotly as py
import plotly.graph_objs as go
from matplotlib import pyplot as plt
import warnings
import os
oldLength = 0
warnings.filterwarnings("ignore",category=plt.cbook.mplDeprecation)
# warnings.filterwarnings("ignore",category=all)
# f, (a1,a2) = plt.subplot(2)
data = None
port = 8050
# from alpha_vantage.timeseries import TimeSeries
dataDict_for_columns = {'distance':0.0, 'temperature': 0.0,'humidity': 0.0, 'time': "", 'year': None, 'month': None, 'day': None, 'date': None}

# key = '7FEDJMHY3CM2KPEC'
# ts = TimeSeries(key, output_format='pandas')

#-------------------------------------------------------------------------------
# Building our Web app and update financial data automatically
# address = '\\\'.join(os.getcwd().split('\\')[:-1])+"\\file.csv"
if os.name=='nt':
    address = os.getcwd()+"\\file.csv"
    # address.
    pp(address)
elif os.name=='posix':
    address = os.getcwd()+"/file.csv"
    # address.
    pp(address)
# ad = "C:/Users/nicol/Desktop/python/sicherheitkopie/PressurePrediction/DataAfterEditing.csv"
# try:
#     df = pd.read_csv(address)
# except:
#     df = pd.DataFrame()
def plotly_plot_data(fig):
    ax_list = fig.axes
    for ax in ax_list:
        if ax.get_legend():

            ax.get_legend().remove()

    fig.tight_layout()
    plotly_fig = mpl_to_plotly(fig, resize=True)
    legend = go.layout.Legend(
        x=0.05,
        y=0.95
    )
    plotly_fig.update_layout(showlegend=True, legend=legend)
    # plotly.offline.plot(plotly_fig, filename="plotly_strain.html")

    return plotly_fig


# fig, (ax1, ax2) = plt.subplots(2)
# df[['phaseTm', 'phaseRm', 'phaseSm']].plot(ax=ax1, title='Pressure of phase T,R & S', label='1/[bar]', alpha=0.8)
# df[['meanTemp']].plot(ax=ax2 , title='rolling mean of Temperature', label = '1/[°C]', alpha = 0.9)
# plotly_fig = plotly_plot_data(fig)
# pp(plotly_fig)
# layout = plotly_fig.layout
# pp(layout)
# plotly_fig.show()
# raise Exception


application = dash.Dash(__name__)

application.layout = html.Div([
    dcc.Graph(id="world_finance", animate=True),   # empty graph to be populated by line chart
    dcc.Interval(
                id='my_interval',
                n_intervals=0,       # number of times the interval was activated
                interval=1*1000,   # update every 2 minutes
    ),
])



#-------------------------------------------------------------------------------
@application.callback(
    Output(component_id='world_finance', component_property='figure'),
    [Input(component_id='my_interval', component_property='n_intervals')]
)
def update_graph(n):
    global oldLength, layout, data
    pp(oldLength)
    try:
        df = pd.read_csv(address)
    except:
        df = pd.DataFrame([], columns=list(dataDict_for_columns.keys()))
    pp(df.shape[0])
    if df.shape[0]>oldLength or not data:
        oldLength = df.shape[0]
        df.set_index('time', inplace=True)
        # pd.DataFrame.plot
        fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(16,10))
        
        df['distance'].plot(ax=ax1, title='distance vs. time', label='1/[mm]', alpha=0.8, color='blue')
        df['temperature'].plot(ax=ax2, title='temperature vs. time', label='1/[°C]', alpha = 0.85, color='red')
        df['humidity'].plot(ax=ax3, title='humidity vs. time', label='1/[pct]', alpha = 0.9, color='black')
        # df[['meanTemp']].plot(ax=ax2 , title='rolling mean of Temperature', label = '1/[°C]', alpha = 0.9)
        # plt.show()
        plotly_fig = plotly_plot_data(fig)
        plotly_fig.update_xaxes(type = 'date')




        # line_chart = px.line(

        #                 data_frame=df,
        #                 x=df.columns.values[0],
        #                 y=df.columns.values[3],
        #                 # color='indicator',
        #                 title="Stock: "
        #              )
        # if plotly_fig:
        data = plotly_fig.data
        # plotly_fig.update_layout()
        layout = plotly_fig.layout
        plt.close(fig=fig)


        return dict(data = data, layout=layout)

    else:
        pp('\n\n\n\nnothing to update here \n\n\n\n')
        return dict(data = data, layout=layout)
        
    # except:
        # pass




#-------------------------------------------------------------------------------
def startMyPlot():

    application.run_server(debug=False, host='0.0.0.0',port=port)

# if __name__ == '__main__':
#     application.run_server(debug=True,port=port)
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