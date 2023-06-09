# -*- coding: utf-8 -*-
"""stock analyzing

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OHgVxcFw7esJTR8DLDIr3gUub8DVzadS
"""

import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

tesla = yf.Ticker('TSLA')

tesla_data = tesla.history(period='max')

tesla_data.reset_index(inplace=True)
tesla_data.head()



"""question 2"""

url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'
html_data = requests.get(url).text

soup=BeautifulSoup(html_data, 'html5lib')

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
tables = soup.find_all('table')
table_index=0
for index, table in enumerate(tables):
    if ('Tesla Quarterly Revenue'in str(table)):
        table_index=index
for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col!=[]):
        date =col[0].text
        revenue =col[1].text.replace("$", "").replace(",", "")
        tesla_revenue=tesla_revenue.append({'Date':date,'Revenue':revenue},ignore_index=True)
tesla_revenue

tesla_revenue = tesla_revenue[tesla_revenue['Revenue']!='']
tesla_revenue

tesla_revenue.tail()



"""QUESTION 3"""

gamestop = yf.Ticker('GME')

gme_data=gamestop.history(period='max')

gme_data.reset_index(inplace=True)
gme_data.head()



"""QUESTION 4"""

html_data = requests.get('https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue').text

soup=BeautifulSoup(html_data, 'html5lib')

gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
tables = soup.find_all('table')
table_index=0
for index, table in enumerate(tables):
    if ('GameStop Quarterly Revenue'in str(table)):
        table_index=index
for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col!=[]):
        date =col[0].text
        revenue =col[1].text.replace("$", "").replace(",", "")
        gme_revenue=gme_revenue.append({'Date':date,'Revenue':revenue},ignore_index=True)
gme_revenue.head()

gme_revenue.tail()



"""QUESTION 5"""

make_graph(tesla_data, tesla_revenue, 'Tesla Historical Share Price & Revenue')



"""QUESTION 6"""

make_graph(gme_data, gme_revenue, 'GameStop')



"""**AUTHOR**

SAI KUMARI PILLI
"""

