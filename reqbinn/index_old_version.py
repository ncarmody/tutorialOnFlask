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

warnings.filterwarnings("ignore",category=plt.cbook.mplDeprecation)
# f, (a1,a2) = plt.subplot(2)

port = 8050
# from alpha_vantage.timeseries import TimeSeries

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
ad = "C:/Users/nicol/Desktop/python/sicherheitkopie/PressurePrediction/DataAfterEditing.csv"
df = pd.read_csv(ad)
def plotly_plot_data(fig):
    ax_list = fig.axes
    for ax in ax_list:
        if ax.get_legend():

            ax.get_legend().remove()

    fig.tight_layout()
    plotly_fig = mpl_to_plotly(fig)
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
                interval=1*10000,   # update every 2 minutes
    ),
])



#-------------------------------------------------------------------------------
@application.callback(
    Output(component_id='world_finance', component_property='figure'),
    [Input(component_id='my_interval', component_property='n_intervals')]
)
def update_graph(n):

    # try:
    df = pd.read_csv(address)
    df.set_index('time', inplace=True)


    fig, (ax1, ax2) = plt.subplots(2)
    df[['phaseTm', 'phaseRm', 'phaseSm']].plot(ax=ax1, title='Pressure of phase T,R & S', label='1/[bar]', alpha=0.8)
    df[['meanTemp']].plot(ax=ax2 , title='rolling mean of Temperature', label = '1/[°C]', alpha = 0.9)
    plotly_fig = plotly_plot_data(fig)




    # line_chart = px.line(

    #                 data_frame=df,
    #                 x=df.columns.values[0],
    #                 y=df.columns.values[3],
    #                 # color='indicator',
    #                 title="Stock: "
    #              )
    # if plotly_fig:
    data = plotly_fig.data
    layout = plotly_fig.layout
    plt.close(fig=fig)


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