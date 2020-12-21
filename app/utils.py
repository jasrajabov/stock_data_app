import datetime
from datetime import timedelta
import plotly.graph_objects as go
from plotly.offline import plot
from plotly.graph_objects import Layout
import pandas as pd
from app.fix_mapping import *


def todays_date():
    return datetime.datetime.now()

def unixTimeConverter(delta):
    today = todays_date()
    if today.weekday() > 4:
        delta_weekday = today.weekday() - 4
        today = today - timedelta(days=delta_weekday)
    time_diff = today - timedelta(days=int(delta))

    str_unix_time = [str(int(today.timestamp())), str(int(time_diff.timestamp()))]
    return str_unix_time[0], str_unix_time[1]

def createChart(data, stock):
    # import ipdb; ipdb.set_trace()
    if not data.get('s') == 'no_data':
        df = pd.DataFrame(data)
        df['t'] = df['t'].apply(lambda t: datetime.datetime.utcfromtimestamp(t))
        layout = Layout(plot_bgcolor='rgba(24, 36, 53, 1)')
        fig = go.Figure(data=[go.Candlestick(x=df['t'],
                        open=df['o'], high=df['h'],
                        low=df['l'], close=df['c'])
                             ], layout=layout)

        fig.update_layout(xaxis_rangeslider_visible=True,
                            autosize=True,
                            width=800,
                            height=400,
                            yaxis_title='{} stock'.format(stock),
                            xaxis_title='Daily price',)

        plt_div = plot(fig, output_type='div')
        # import ipdb; ipdb.set_trace()
    else:
        plt_div = 'no data for chart for today'
    return plt_div


def getKeyByValue(dict, value):
    keys = list(dict.keys())
    values = list(dict.values())

    position = values.index(value)
    key = keys[position]
    return key

def fix_splitter(fix_message, message_type):
    splittedFix = fix_message.__str__().split('|')
    pairedFix = [fix.split('=') for fix in splittedFix]
    fixTagValues = [tag for tag,value in pairedFix]
    fixTagDesc = []

    if message_type == 'New Order Single':
        for tag in fixTagValues:
                key = getKeyByValue(new_order_single, int(tag))
                fixTagDesc.append(key)
    # import ipdb; ipdb.set_trace()
    pairedWithDesciption = list(zip(fixTagDesc, pairedFix))
    return pairedWithDesciption
