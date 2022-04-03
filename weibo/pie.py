import plotly.offline as py
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go
import requests
import re
import json
import time
import os
import csv


def draw_pie(labels, values):
    # py.init_notebook_mode(connected=True)

    trace = [
        go.Pie(
            labels=labels,
            values=values,
            # hole=0.7,
            hoverinfo='label+percent',  # hoverinfo属性用于控制当用户将鼠标指针放到环形图上时，显示的内容
            # pull=[0.1, 0, 0, 0, 0],  # 弹出效果
        )
    ]
    layout = go.Layout(
        title='分析图',
        titlefont=dict(size=30),
        showlegend=True,
        legend=dict(
            x=0.8,
            y=1
        ),

    )
    fig = go.Figure(data=trace, layout=layout)
    fig.write_html('D:\codefield\python\weibo_site\weibo\\templates\weibo\\'+'pic.html')
    # py.plot(fig)


def get_pie_html():
    data = []
    with open('weibo\emotion.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for each in enumerate(reader):
            data.append(each[1])

    num = [0, 0, 0]
    headers = ['positive', 'negative', 'mid']
    for each in data:
        if each[9] == 'positive':
            num[0] += 1
        elif each[9] == 'negative':
            num[2] += 1
        else:
            num[1] += 1
    draw_pie(headers, num)
# get_pie_html()