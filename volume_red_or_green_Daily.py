import talib as ta
from ta.utils import dropna
import yfinance as yf
import pandas as pd
import sys
import re
import numpy as np
from talib import stream
from matplotlib import dates
import matplotlib.pyplot as plt
##from datetime import date
##today = date.today().isoformat()
import datetime
import math
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
plt.style.use('fivethirtyeight')
from millify import millify
##today = datetime.date.today() + datetime.timedelta(days=1)
today = datetime.date.today()
##day = datetime.datetime.strptime(Date, '%d %m %Y').weekday()
##print(datetime.today().strftime('%Y-%m-%d'))
import mplfinance
import matplotlib
import sys
##from matplotlib.finance import candlestick2_ohlc
##from mpl_finance import candlestick_ohlc
##from mplfinance.original_flavor import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc
from optionprice import Option
from numerize import numerize
import matplotlib.pyplot as plt
pd.options.display.width = 0
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:.2f}'.format
##pd.options.display.max_columns=255
pd.options.display.max_rows=6500000
pd.set_option('display.max_colwidth', 500)
pd.set_option('display.max_columns', 550)
pd.options.mode.chained_assignment = None  # default='warn'
import time
from datetime import datetime

import sys
import time


start=time.time()


perda='15d'
intervla='30m'
yy=str(intervla).split('d')[0]
shiftbydays=3



##    g=input("Entr_Signal ticker: ")
perd=perda
#intervl='1m'
intervl='5dd'

##ticker=input("===========  Enter ticker: =========== ")
##ticker='BTC-USD'
##ticker='TSLA'
##ticker='NVDA'
##ticker='^dji'
#ticker='^ndx'
##ticker='^gspc'
##ticker='^ndx'
ticker='spy'
##ticker='qqq'


#gg=['arkk','^ndx','^gspc','^dji','spy','tna','qqq','tsla','^dji']
print('\n')
##ticker=input("Enter ticker:")
print('\n')
df = yf.download(ticker, period=perd, interval=intervla,prepost = True)
##df = yf.download(ticker, period=perd, interval='5m',prepost = True)
df=pd.DataFrame(df)

df.reset_index(inplace=True,drop=False)
df.rename(columns={'index': 'Datetime'}, inplace=True)
#print(df.tail(4))






df['Candlea']=''
df['*']=''
for x in df.index:    
    df['Candlea'].loc[x]=df['High'].loc[x]-df['Open'].loc[x]
    df['*'].loc[x]='*'

df['Opena']=''
df['green']=''
df['greenby']=''
df['compare_d']=''

df['Candle']=''
df['direct']=''
df['down']=''
df['a_Close']=''
df['a_High']=''
df['a_Low']=''
df['a_Open']=''
df['HA']=''
df['upward_pressure']=''
df['downward_pressure']=''
df['HA->']=''
df['MA->']=''
df['CCI/RSI->']=''
df['Close->']=''
df['intervl']=''
df['ticker']=''



df['PLUS_DI']=ta.PLUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14)
df['PLUS_DM']=ta.PLUS_DM(df['High'],df['Low'], timeperiod=14)
#################################################################
for x in df.index:
    df['compare_d'].loc[x]=str(shiftbydays)+'d'   
    df['Opena'].loc[x]=int(df['Open'].loc[x])
    if df['Close'].loc[x]-df['Open'].loc[x] > 0:
        df['green'].loc[x]='Green'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
        #            print(x,'  ','Green','  ',df['ns'].loc[x])
    else:
        df['green'].loc[x]='Red'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]


########################################################################
df['Closev'] = (1/df['Close'])*(100)
for x in df.index:
    df['Closev'].loc[x]=df['Closev'].loc[x]
    df['upward_pressure'].loc[x]=df['PLUS_DM'].loc[x]-df['PLUS_DI'].loc[x]
    df['downward_pressure'].loc[x]=df['PLUS_DI'].loc[x]-df['PLUS_DM'].loc[x]
    df['Candle'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]

    df['HA->'].loc[x]='HA->'
    df['Close->'].loc[x]='Close->'
    df['*'].loc[x]='*'
    df['MA->'].loc[x]='MA->'
    df['CCI/RSI->']='CCI/RSI->'
    
    

    df['intervl'].loc[x]=intervl
    df['ticker'].loc[x]=ticker
##    df['Close_d_ch'].loc[x]=df['Close'].loc[x]-df['Close_d'].loc[x]
    df['Opena'].loc[x]=int(df['Open'].loc[x])
    if df['Close'].loc[x]-df['Open'].loc[x] > 0:
        df['green'].loc[x]='Green'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
        #            print(x,'  ','Green','  ',df['ns'].loc[x])
#    elif:
#        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
        #            print(x,'  ','Green','  ',df['ns'].loc[x])
    else:
        df['green'].loc[x]='Red'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]


    df['a_Close'].loc[x]=1/4*(df['Open'].loc[x]+df['High'].loc[x]+df['Low'].loc[x]+df['Close'].loc[x])
    df['a_Open'].loc[x]=1/2*(df['Open'].shift(1).loc[x]+df['Close'].shift(1).loc[x])
    df['High'].loc[x]=df['High'].loc[x]
    df['Low'].loc[x]=df['Low'].loc[x]
    df['a_High'].loc[x]=max(df['High'].loc[x],df['a_Open'].loc[x],df['a_Close'].loc[x])
    df['a_Low'].loc[x]=min(df['Low'].loc[x],df['a_Open'].loc[x],df['a_Close'].loc[x])


 #   df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])
    df['HA'].loc[x]=df['a_Close'].loc[x]-df['a_Open'].loc[x]
##    df2['d']=df2['Datetime'].dt.day_name()
#    print(df2)

#   if df2['a_Close'].loc[x] > df2['a_Open'].loc[x]:
    if df['HA'].loc[x] > 0:
        df['direct'].loc[x]='HA_Green'
    elif df['HA'].loc[x] < 0:
        df['direct'].loc[x]='HA_Red'


df['s3']=''
for x in df.index:
    df['s3'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[0]

          
#print(df)
cc=df.groupby(['s3', 'green']).sum()
df3=pd.DataFrame(cc['Volume'])
df3.reset_index(inplace=True,drop=False)
#print(df3)
df3['delta']=0.0
df3['ticker']=''
df3['Closex']=''
df3['sold_buy_%']=''


############ calculate % of volume ###############3333
for x in df3.index:
    if df3['s3'].loc[x]==df3['s3'].shift(1).loc[x]:
        df3['delta'].loc[x]=df3['Volume'].shift(1).loc[x]-df3['Volume'].loc[x]
        if df3['delta'].loc[x] < 0:
            df3['sold_buy_%'].loc[x]=-1*(df3['Volume'].loc[x]/df3['Volume'].shift(1).loc[x])*100
        if df3['delta'].loc[x] > 0:
            df3['sold_buy_%'].loc[x]=(df3['Volume'].loc[x]/df3['Volume'].shift(1).loc[x])*100    
        df3['ticker'].loc[x]=ticker
 ############ calculate % of volume ###############3333
#print('\n\n')
#print(df3,'   peter')
#print('\n\n')
df4=df3.pivot(index='s3',columns=['green'],values=['ticker','sold_buy_%','Volume','delta'])
#print('\n\n')
#print(df4,'  sam')
df4=pd.DataFrame(df4)
df4.reset_index(inplace=True,drop=False)





df4["s3"] = pd.to_datetime(df4["s3"])
#print('\n\n')
df4['weekday'] =df4['s3'].dt.day_name()
df4.set_index('s3',inplace=True)
#print('\n\n')
df4.drop(df4.columns[6], axis=1,inplace=True)
df4.drop(df4.columns[2], axis=1,inplace=True)

df4.rename(columns={df4.columns[3]: 'new'})
df4.columns=['a','Ticker','%','Vol_Buy_Green','Vol_Sold_Red','Delta','Day']
df4['Total_Vol']=''






for x in df4.index:
    df4['Total_Vol'].loc[x]=df4['Vol_Buy_Green'].loc[x]+df4['Vol_Sold_Red'].loc[x]
##    df4['Closeff'].loc[x]=df4['Close'].loc[df4.shape[0]-1]
df4.reset_index(inplace=True)
df4.set_index(['s3','Day','Ticker'],inplace=True)
df4=df4[['Total_Vol','Vol_Buy_Green','Vol_Sold_Red','Delta','%']]
#print('\n\n')

df4['%_of_volume_bought_or_sold']=''
############ calculate % of volume ###############3333
for x in df4.index:    
##    if df4['Delta'].loc[x] > 0:
##        df4['%'].loc[x]=100*float(float(df4['Delta'].loc[x]))/df4['Total_Vol'].loc[x]
##    if df4['Delta'].loc[x] < 0:
##        df4['%'].loc[x]=100*float(float(df4['Delta'].loc[x]))/df4['Total_Vol'].loc[x]
####        df4['%'].loc[x]=((df4['Delta'].loc[x]))/df4['Total_Vol'].loc[x]*float(100)

    if df4['Delta'].loc[x] > 0:
        df4['%'].loc[x]=100*float(float(df4['Vol_Buy_Green'].loc[x]))/df4['Total_Vol'].loc[x]
        df4['%'].loc[x]=round(df4['%'].loc[x],2)
        df4['%_of_volume_bought_or_sold'].loc[x]=str(df4['%'].loc[x])+ str(' % of total_vol [bought]')
    if df4['Delta'].loc[x] < 0:
        df4['%'].loc[x]=-1*100*float(float(df4['Vol_Sold_Red'].loc[x]))/df4['Total_Vol'].loc[x]
        df4['%'].loc[x]=round(df4['%'].loc[x],2)
        df4['%_of_volume_bought_or_sold'].loc[x]=str(df4['%'].loc[x])+ str(' % of total_vol [sold]')


 ############ calculate % of volume ###############3333  



for x in df4.index:
    df4['Total_Vol'].loc[x]=numerize.numerize(np.float32(df4['Total_Vol'].loc[x]).item())
    df4['Delta'].loc[x]=numerize.numerize(np.float32(df4['Delta'].loc[x]).item())
    df4['Vol_Sold_Red'].loc[x]=numerize.numerize(np.float32(df4['Vol_Sold_Red'].loc[x]).item())
    df4['Vol_Buy_Green'].loc[x]=numerize.numerize(np.float32(df4['Vol_Buy_Green'].loc[x]).item())
    

##df4.reset_index(inplace=True)
##df4=df4[['Total_Vol','Vol_Buy_Green','Vol_Sold_Red','Delta','%_of_Volume_bought_or_sold']]
df4.drop(df4.columns[4], axis=1,inplace=True)

###print(df4,'  joe')
##print(df4.iloc[:,4])
#print('\n\n')
df4.reset_index(inplace=True)
df4.set_index('s3',inplace=True)


df7 = yf.download(ticker, period=perd, interval='1d',prepost = True)
##df = yf.download(ticker, period=perd, interval='5m',prepost = True)
df7=pd.DataFrame(df7)
##print(df7)

result = pd.concat([df4, df7], axis=1)

for x in result.index:
    result['Volume'].loc[x]=numerize.numerize(np.float32(result['Volume'].loc[x]).item())

print(result)


