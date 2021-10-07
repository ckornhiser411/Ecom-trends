import requests
import pytrends


import pandas as pd
from pytrends.request import TrendReq  #Request connection to google to view trending topics

pytrends = TrendReq()

kw_list = ["Arts and Crafts","Sow"]
pytrends.build_payload(kw_list, cat=1361, timeframe='today 5-y', geo='US', gprop='') #1361 = Arts and Craft Supplies

pytrends.interest_over_time()

df_interest = pytrends.interest_over_time()

df_interest.head()

df_interest.to_csv("Ecom_Trends.csv")
