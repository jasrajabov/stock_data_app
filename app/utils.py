import datetime
from datetime import timedelta
import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd


def unixTimeConverter(delta):
    now = datetime.datetime.now()
    time_diff = now - timedelta(days=int(delta))

    str_unix_time = [str(int(now.timestamp())), str(int(time_diff.timestamp()))]
    return str_unix_time[0], str_unix_time[1]

def createChart(data):
    # import ipdb; ipdb.set_trace()
    df = pd.DataFrame(data)
    # import ipdb; ipdb.set_trace()
    df['t'] = df['t'].apply(lambda t: datetime.datetime.utcfromtimestamp(t))
    # .strftime(
        # '%Y-%m-%d %H:%M:%S'))
    # import ipdb; ipdb.set_trace()

    fig = go.Figure(data=[go.Candlestick(x=df['t'],
                    open=df['o'], high=df['h'],
                    low=df['l'], close=df['c'])
                         ])

    fig.update_layout(xaxis_rangeslider_visible=False,
                        autosize=False,
                        width=1000,
                        height=500,)
    plt_div = plot(fig, output_type='div')
    return plt_div
