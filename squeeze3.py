import os, pandas
import plotly.graph_objects as go
import yfinance as yf
import pandas as pd
import datetime as dt
import talib as ta

pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns=255
pd.options.display.max_rows=6500000

pd.options.display.max_rows=9999
pd.options.display.max_columns=36
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)

##dataframes = {}

def chart_babu(df,x):
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib
    import talib as ta
    import os, pandas



    df['EMA_3s']=ta.EMA(df['Close'], timeperiod=3)
    df['EMA_5s']=ta.EMA(df['Close'], timeperiod=5)
    df['EMA_10s']=ta.EMA(df['Close'], timeperiod=10)

    df['EMA_21s']=ta.EMA(df['Close'], timeperiod=21)
    df['MOM']=ta.MOM(df['Close'], timeperiod=10)
    df['EMA_50s']=ta.EMA(df['Close'], timeperiod=50)
    df['EMA_100s']=ta.EMA(df['Close'], timeperiod=100)
    df['MOM']=ta.MOM(df['Close'], timeperiod=10)

    
    v = df['Volume'].values
    tp = (df['Low'] + df['Close'] + df['High']).div(3).values
    df = df.assign(vwap=(tp * v).cumsum() / v.cumsum())
    print('\n','*************************** ',df)


    
    df.reset_index(inplace=True)
    fig, ax = plt.subplots()
    plt.xlabel("Date")
    plt.ylabel("Close")



##    plt.hist(df['MOM'], density=True, bins=30)

    plt.plot(df['Date'],df['vwap'],color = 'violet',label='vwap', linestyle='--', lw=4)
    plt.plot(df['Date'],df['EMA_3s'],color = 'r',label='EMA_3s', linestyle='--', lw=1)
    plt.plot(df['Date'],df['EMA_3s'],color = 'r',label='EMA_3s', linestyle='--', lw=1)
    plt.plot(df['Date'],df['EMA_5s'],color = 'c',label='EMA_5s', linestyle='--', lw=1)
    plt.plot(df['Date'],df['EMA_10s'],color = 'magenta',label='EMA_10s', linestyle='--', lw=1)
    
    plt.plot(df['Date'],df['EMA_21s'],color = 'y',label='EMA_21s', linestyle='--', lw=1)
    plt.plot(df['Date'],df['EMA_50s'],color = 'b',label='EMA_50s', linestyle='--', lw=1)
    plt.plot(df['Date'],df['EMA_100s'],color = 'c',label='EMA_100s', linestyle='--', lw=1) 
##    df.reset_index(inplace=True)
    #print(df)
    plt.plot(df['Date'],df['bolinger_upper_band'],color = 'r',label='Upper Bollinger Band')
    plt.plot(df['Date'],df['bolinger_lower_band'],color = 'r',label='Lower Bollinger Band')

    plt.plot(df['Date'],df['upper_keltner'],color = 'b',label='Upper Keltner Channel')
    plt.plot(df['Date'],df['lower_keltner'],color = 'b',label='Lower Keltner Channel')
    plt.plot(df['Date'],df['Close'],color = 'g',label='Close')

##    plt.plot(df['Date'],df['Close>50'],color = 'y',label='Close>50')
    
##    plt.bar(df3['Datetime'],df3['Cl_del'],color = 'b',width = 1.25,label='Cl_del')
##    plt.bar(df3['Date'],df3['aroonup'],color = 'g',width = .55,label='aroonup')
##    plt.bar(df3['Date'],df3['aroondown'],color = 'r',width = .45,label='aroondown')
####    plt.bar(df3['Date'],df3['5>10'],color = 'y',width = .85,label='5>10')
##    plt.bar(df3['Date'],df3['50>vwap'],color = 'y',width = .45,label='50>vwap')
##    plt.bar(df3['Date'],df3['21>50'],color = 'c',width = .45,label='21>50')
##    plt.xticks(None, rotation=44)
##    plt.plot(df3['Date'],df3['Cl_del'],'-r',label='Closed-delta')

    mm=round(df['Close'].loc[df.shape[0]-1],0)
    m=round(df['Close'].loc[df.shape[0]-1]-df['Close'].loc[df.shape[0]-2],0)
##    m=(df['Close'].tail(1)).to_string(index=False)-(df['Close'].loc[tail(2)-df.shape[0]-1]).to_string(index=False)
    plt.title(x+'   '+str(mm)+'/'+str(m))
    plt.legend(loc="upper left")
    
    plt.show()


##uu=['t','aa']



uu4=['vg','astr','ispc','mpln','nbev','avya','cei','nvts','now','snow','amc','aapl','f','asml','zm',
    'tsla','nio','plug','lcid','rivn','fsr','blnk','mrna','bntx','nvax','bntx','isrg','biib','pfe','abt',
    'qcom','nvda','avgo','qrvo','gfs','tsm',
    'adbe','gme','nvda','nflx','asml','mu','avgo','amd','asml','qcom','mrvl','txn','intc,dltr','penn','coin','mstr','uber','lyft','z',
    '^ndx','RSX','AUPH','BHP', 'DUST', 'EWY', 'NYCB', 'QID', 'SQQQ', 'SVRA', 'AEP',
    'BHP', 'DUST', 'EWY', 'NYCB', 'QID', 'SQQQ', 'SVRA', 'AEP',
    'bby','zm','dks','anf','dltr','xpev','arkk','^ndx','^gspc','^dji','spy','tna','qqq','tsla','^dji','pfe','f','intc','spy']

uu=['mstr']   


for x in uu:
    
##    symbol = filename.split(".")[0] '^ndx','^gspc','^dji','spy','amzn','googl']
    #print(symbol)
    df=yf.Ticker(x).history(period ='100d', interval = '1d',prepost = True)
    df=pd.DataFrame(df)

    
##    df['EMA_50s']=ta.EMA(df['Close'], timeperiod=50)
##    print(df['EMA_21s'].loc[x],'   ',df['EMA_50s'].loc[x])
##    df['MOM']=ta.MOM(df['Close'], timeperiod=10)
##    df['Close>50']=''
##    df['Close>21']=''
##    if df.empty:
##        continue

    df['ticker']=''
    for p in df.index:
        df['ticker'].loc[p]=x

    df=df[['ticker','Open', 'High', 'Low', 'Close', 'Volume'] ]
##    df['Close>50'].loc[x]=df['Close'].loc[x]-df['EMA_50s'].loc[x]
##    df['Close>100'].loc[x]=df['Close'].loc[x]-df['EMA_100s'].loc[x]

    df['20sma'] = df['Close'].rolling(window=20).mean()
    df['stddev'] = df['Close'].rolling(window=20).std()
    df['bolinger_lower_band'] = df['20sma'] - (2 * df['stddev'])
    df['bolinger_upper_band'] = df['20sma'] + (2 * df['stddev'])

    df['TR'] = abs(df['High'] - df['Low'])
    df['ATR'] = df['TR'].rolling(window=20).mean()

    df['lower_keltner'] = df['20sma'] - (df['ATR'] * 1.5)
    df['upper_keltner'] = df['20sma'] + (df['ATR'] * 1.5)
    df=df[['ticker','Open', 'High', 'Low', 'Close', 'Volume', 'bolinger_lower_band',
           'bolinger_upper_band','upper_keltner','lower_keltner']]
##    print(df)

##    def in_squeeze(df):
##        return df['bolinger_lower_band'] > df['lower_keltner'] and df['bolinger_upper_band'] < df['upper_keltner']

    df['squeeze_on'] =''
    for z in df.index:
        if df['bolinger_lower_band'].loc[z] > df['lower_keltner'].loc[z] or df['bolinger_upper_band'].loc[z] < df['upper_keltner'].loc[z]:
            df['squeeze_on'].loc[z]='in_squeeze'
        else:
            df['squeeze_on'].loc[z]=' '

##
##    df['squeeze_on'] = df.apply(in_squeeze, axis=1)

##    if df.iloc[-3]['squeeze_on'] and not df.iloc[-1]['squeeze_on']:
##        print("{} is coming out the squeeze".format(symbol))

    df.reset_index(inplace=True)
    df=df[['Date','Open', 'High', 'Low', 'Close', 'Volume', 'ticker','bolinger_lower_band', 'bolinger_upper_band',
           'lower_keltner', 'upper_keltner',
##           '20sma', 'stddev',
##           'bolinger_lower_band', 'bolinger_upper_band', 'TR', 'ATR', 'lower_keltner', 'upper_keltner',
           'squeeze_on']]
    df = df.dropna()
    print(df)

    

    cc=[]
    for x2 in df.index:
        if len(df['squeeze_on'].loc[x2]) > 0:
            print('in squeeze','\n',df['ticker'].loc[x2],'\n',
                  df.loc[x2])
            
##            if df['squeeze_on'].loc[x2]  != ' ':
            cc.append(x)
            break


##    if df['squeeze_on'].tail(1).to_string(index=False)=='in_squeeze':
##        chart_babu(df,x)                   

    chart_babu(df,x)



