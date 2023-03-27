
import talib as ta
import yfinance as yf
import pandas as pd
import datetime as dt
import sys
import re
import numpy as np
from talib import stream
import matplotlib.pyplot as plt
##from datetime import date
##today = date.today().isoformat()
import datetime
import math
from millify import millify
##today = datetime.date.today() + datetime.timedelta(days=1)
today = datetime.date.today()
##print(datetime.today().strftime('%Y-%m-%d'))
import mpl_finance
import matplotlib
##from matplotlib.finance import candlestick2_ohlc
##from mpl_finance import candlestick_ohlc
##from mplfinance.original_flavor import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc
from optionprice import Option
from numerize import numerize

pd.options.display.width = 0
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:.2f}'.format
##pd.options.display.max_columns=255
pd.options.display.max_rows=6500000
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)


def days():
    
    perda='635d'
    intervla='1d'


    ##    g=input("Entr_Signal ticker: ")
    perd=perda
    intervl=intervla

    # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]



    #df=pd.DataFrame()
    #Interval required 5 minutes
    df = yf.download('^NDX', period=perd, interval=intervl,prepost = True)
    df2=pd.DataFrame()
    df['*']=''
    for x in df.index:
        df['*'].loc[x]='*'
    ##    print(df['Close'].loc[x])
        ########################################################

    ##close = numpy.random.random(100)
    CCI=ta.CCI(df['High'],df['Low'],df['Close'],timeperiod=5)
    DX=ta.DX(df['High'],df['Low'],df['Close'],timeperiod=5)
    WILLR=ta.WILLR(df['High'],df['Low'],df['Close'],timeperiod=5)
    RSI = ta.RSI(df['Close'], timeperiod=14)
    stoch_slowk, stoch_slowd = ta.STOCH(df['High'],df['Low'],df['Close'], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    STOCHRSI_fastk, STOCHRSI_fastd = ta.STOCHRSI(df['Close'], timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
    macd, macdsignal, macdhist = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    adx = ta.ADX(df['High'],df['Low'],df['Close'], timeperiod=14)
    WilliamsR= ta.WILLR(df['High'],df['Low'],df['Close'], timeperiod=14)
    ATR=ta.ATR(df['High'],df['Low'],df['Close'], timeperiod=14)
    ULTOSC = ta.ULTOSC(df['High'],df['Low'],df['Close'], timeperiod1=7, timeperiod2=14, timeperiod3=28)
    ROC = ta.ROC(df['Close'], timeperiod=10)
    PLUS_DI=ta.PLUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14)
    PLUS_DM=ta.PLUS_DM(df['High'],df['Low'], timeperiod=14)
    AROON=ta.AROON(df['High'],df['Low'], timeperiod=14)
    HT_DCPERIOD=ta.HT_DCPERIOD(df['Close'])
    HT_DCPHASE=ta.HT_DCPHASE(df['Close'])
    sine, leadsine=ta.HT_SINE(df['Close'])
##    macd, macdsignal, macdhist=ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
##    PLUS_DI=ta.PLUS_DI(df['High'],df['Low'],df['Close'], timeperiod=14),
##    PLUS_DM=ta.PLUS_DM(df['High'],df['Low'], timeperiod=14),
##    PPO=ta.PPO(df['Close'], fastperiod=12, slowperiod=26, matype=0),
##    ROC=ta.ROC(df['Close'], timeperiod=10),
##    ROCP=ta.ROCP(df['Close'], timeperiod=10),
##    ROCR=ta.ROCR(df['Close'], timeperiod=10),
##    ROCR100=ta.ROCR100(df['Close'], timeperiod=10),

    CDLDOJI=ta.CDLDOJI(df['Open'], df['High'],df['Low'],df['Close'])
    CDLDOJISTAR=ta.CDLDOJISTAR(df['Open'], df['High'],df['Low'],df['Close'])
    CDLDRAGONFLYDOJI=ta.CDLDRAGONFLYDOJI(df['Open'], df['High'],df['Low'],df['Close'])
    CDLEVENINGDOJISTAR=ta.CDLEVENINGDOJISTAR(df['Open'], df['High'],df['Low'],df['Close'], penetration=0)
    CDLGRAVESTONEDOJI=ta.CDLGRAVESTONEDOJI(df['Open'], df['High'],df['Low'],df['Close'])
    CDLHAMMER=ta.CDLHAMMER(df['Open'], df['High'],df['Low'],df['Close'])
    CDLXSIDEGAP3METHODS=ta.CDLXSIDEGAP3METHODS(df['Open'], df['High'],df['Low'],df['Close'])
    aroondown, aroonup = ta.AROON(df['High'],df['Low'], timeperiod=3)


    EMA_3=df['Close']-ta.EMA(df['Close'], timeperiod=3)
    EMA_5=df['Close']-ta.EMA(df['Close'], timeperiod=5)
    EMA_10=df['Close']-ta.EMA(df['Close'], timeperiod=10)
    EMA_21=df['Close']-ta.EMA(df['Close'], timeperiod=21)
    EMA_50=df['Close']-ta.EMA(df['Close'], timeperiod=50)
    EMA_100=df['Close']-ta.EMA(df['Close'], timeperiod=100)
    EMA_200=df['Close']-ta.EMA(df['Close'], timeperiod=200)


    EMA_3s=ta.EMA(df['Close'], timeperiod=3)
    EMA_5s=ta.EMA(df['Close'], timeperiod=5)
    EMA_10s=ta.EMA(df['Close'], timeperiod=10)
    EMA_21s=ta.EMA(df['Close'], timeperiod=21)
    EMA_50s=ta.EMA(df['Close'], timeperiod=50)
    EMA_100s=ta.EMA(df['Close'], timeperiod=100)
    EMA_200s=ta.EMA(df['Close'], timeperiod=200)


    #############################
    ##for x in df.index:
    ##            df['Volume'].loc[x]=numerize.numerize(np.float32(df['Volume'].loc[x]).item())

    df2=df

    df['Opena']=''
    df['green']=''
    df['greenby']=''

    for x in df.index:

##        df['Close_ch'].loc[x]=df['Close'].loc[x]-df['Close'].shift(1).loc(x)
        df['Opena'].loc[x]=int(df['Open'].loc[x])
        if df['Close'].loc[x]-df['Open'].loc[x] > 0:



            df['green'].loc[x]='Green'
            df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
                                            #            print(x,'  ','Green','  ',df['ns'].loc[x])
        else:

            df['green'].loc[x]='Red'
            df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
    ##print(df)
    ##print('\n',' 1-day    ',g,'\n')

    df2['direct']=''
    df2['down']=''
    df2['a_Close']=''
    df2['a_High']=''
    df2['a_Low']=''
    df2['a_Open']=''
    df2['HA']=''
    df2['Opena']=''
    df2['green']=''
    df2['greenby']=''
    df2['Volumea']=''

    for x in df.index:
       

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
    ##    df2['d']=df2['Date'].dt.day_name()
    #    print(df2)

    #   if df2['a_Close'].loc[x] > df2['a_Open'].loc[x]:
        if df['HA'].loc[x] > 0:
            df['direct'].loc[x]='HA_Green'
        elif df['HA'].loc[x] < 0:
            df['direct'].loc[x]='HA_Red'

        df['Volumea']=(df['Volume']-df['Volume'].shift(1))
    ############################ end of ha




    ##ddd=(df['Volume']-df['Volume'].shift(1))
    tt=pd.concat([df['direct'],df['HA'],df['Close'],(df['Close']-df['Close'].shift(1)),df['Volume'],
                  df['Volumea'],CCI,DX,WILLR,RSI,adx,WilliamsR,ATR,ULTOSC,ROC,PLUS_DI,PLUS_DM,
                  HT_DCPERIOD,
                  HT_DCPHASE,
                  sine,leadsine,aroondown, aroonup,
##                  macd, macdsignal, macdhist,PLUS_DI,PLUS_DM,PPO,ROC,ROCP,ROCR,ROCR100,
                  df['*'],
                  CDLDOJI,CDLDOJISTAR,CDLDRAGONFLYDOJI,CDLEVENINGDOJISTAR,CDLGRAVESTONEDOJI,CDLHAMMER,CDLXSIDEGAP3METHODS,
                  df['*'],EMA_3,EMA_5,EMA_10,EMA_21,EMA_50,EMA_100,EMA_200,EMA_3s,EMA_5s,EMA_10s,EMA_21s,EMA_50s,EMA_100s,EMA_200s],axis=1)

    print(tt.tail(4))
    print('tt-columns:',tt.columns)
    
    sys.exit()
    tt.columns=['direct','HA','Close','Close_ch','Volume','Volumea','CCI','RSI','DX','WILLR',
                'adx','WilliamsR','ATR','ULTOSC','ROC','PLUS_DI','PLUS_DM',
                "*",'CDLDOJI','CDLDOJISTAR','CDLDRAGONFLYDOJI','CDLEVENINGDOJISTAR','CDLGRAVESTONEDOJI','CDLHAMMER','CDLXSIDEGAP3METHODS','HT_DCPERIOD',
                'HT_DCPHASE',
                'sine','leadsine','aroondown', 'aroonup',
##                'macd', 'macdsignal', 'macdhist','PLUS_DI','PLUS_DM','PPO','ROC','ROCP','ROCR','ROCR100',
                
                '*','EMA_3','EMA_5','EMA_10','EMA_21','EMA_50','EMA_100','EMA_200',
                'EMA_3s','EMA_5s','EMA_10s','EMA_21s','EMA_50s','EMA_100s','EMA_200s' 
                ]

    tt.reset_index(inplace=True)        
    for x in tt.index:
    ##    print(tt['Volume'])
    ##    tt['Volume'].loc[x]=numerize.numerize(tt['Volume'].loc[x])
    ##    tt['Volume'].loc[x]=numerize.numerize((tt['Volume'].iloc[x][1]))
        tt['Volume'].loc[x]=numerize.numerize(np.float32(tt['Volume'].loc[x]).item())
    tt.set_index('Date')
    print('\n',tt.columns,'\n')
    print(tt.columns.get_loc('CCI'))

    gg33=tt.iloc[:,[0,1,2,3,4,7,10]].tail(135)
    print(gg33)
    
    print('\n\n\n')
    print('CCI > 100 --> down   CCI < -100 ----> Up',)
    print('\n','RSI : RSI between 70, 20. > 70 overbought, < 20 oversold')
    print('\n','ULOST: Buy signal ULOST < 30 , sell signal ULOS > 70')
    
    print('\n','DX:  The DX is usually smoothed with a moving average (i.e. the ADX).The values range from 0 to 100, but rarely get above 60.To interpret the DX, consider a high number to be a strong trend, and a low number, a weak trend.')
    print('\n','WilliamR between -20 and -80. -20 is overbought/highs of its recent range, -80 is oversold/lower end of its recent range.')
    print('\n','ADX : Strength of trend, 0-25 -> Absent or Weak Trend,    25-50 --> Strong Trend, ? --> 50-75, 75-100-->Extremely Strong Trend')
    print('\n','ATR : ATR indicates increased volatility in the market')
    

##    print('Daily CCI: ', tt.tail(4))
    ##MA = ta.SMA(df['close'])
    ##print('MA: ',MA)
    #########################################################################################################################

    ##from talib import MA_Type
    ##upper, middle, lower = talib.BBANDS(close, matype=MA_Type.T3)
    ##print('bolinger_bands: ', upper,'  ', middle,'  ',lower)

def hourly():
    from numerize import numerize

    
    perda='2d'
    intervla='1m'


    ##    g=input("Entr_Signal ticker: ")
    perd=perda
    intervl=intervla

    # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]



    #df=pd.DataFrame()
    #Interval required 5 minutes
    df = yf.download('^NDX', period=perd, interval=intervl,prepost = True)

##    data = yf.download(g, period=perd, interval=intervl,prepost = True)

    
    df2=pd.DataFrame()
    df['*']=''
    for x in df.index:
        df['*'].loc[x]='*'
    ##    print(df['Close'].loc[x])
        ########################################################

    ##close = numpy.random.random(100)
    CCI=ta.CCI(df['High'],df['Low'],df['Close'],timeperiod=5)
    DX=ta.DX(df['High'],df['Low'],df['Close'],timeperiod=5)
    WILLR=ta.WILLR(df['High'],df['Low'],df['Close'],timeperiod=5)

    CDLDOJI=ta.CDLDOJI(df['Open'], df['High'],df['Low'],df['Close'])
    CDLDOJISTAR=ta.CDLDOJISTAR(df['Open'], df['High'],df['Low'],df['Close'])
    CDLDRAGONFLYDOJI=ta.CDLDRAGONFLYDOJI(df['Open'], df['High'],df['Low'],df['Close'])
    CDLEVENINGDOJISTAR=ta.CDLEVENINGDOJISTAR(df['Open'], df['High'],df['Low'],df['Close'], penetration=0)
    CDLGRAVESTONEDOJI=ta.CDLGRAVESTONEDOJI(df['Open'], df['High'],df['Low'],df['Close'])
    CDLHAMMER=ta.CDLHAMMER(df['Open'], df['High'],df['Low'],df['Close'])
    CDLXSIDEGAP3METHODS=ta.CDLXSIDEGAP3METHODS(df['Open'], df['High'],df['Low'],df['Close'])


    EMA_3=df['Close']-ta.EMA(df['Close'], timeperiod=3)
    EMA_5=df['Close']-ta.EMA(df['Close'], timeperiod=5)
    EMA_10=df['Close']-ta.EMA(df['Close'], timeperiod=10)
    EMA_21=df['Close']-ta.EMA(df['Close'], timeperiod=21)
    EMA_50=df['Close']-ta.EMA(df['Close'], timeperiod=50)
    EMA_100=df['Close']-ta.EMA(df['Close'], timeperiod=100)
    EMA_200=df['Close']-ta.EMA(df['Close'], timeperiod=200)


    #############################
    ##for x in df.index:
    ##            df['Volume'].loc[x]=numerize.numerize(np.float32(df['Volume'].loc[x]).item())

    df2=df

    df['Opena']=''
    df['green']=''
    df['greenby']=''

    for x in df2.index:
        df['Opena'].loc[x]=int(df['Open'].loc[x])
        if df['Close'].loc[x]-df['Open'].loc[x] > 0:



            df['green'].loc[x]='Green'
            df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
                                            #            print(x,'  ','Green','  ',df['ns'].loc[x])
        else:

            df['green'].loc[x]='Red'
            df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
    ##print(df)
    ##print('\n',' 1-day    ',g,'\n')

    df2['direct']=''
    df2['down']=''
    df2['a_Close']=''
    df2['a_High']=''
    df2['a_Low']=''
    df2['a_Open']=''
    df2['HA']=''
    df2['Opena']=''
    df2['green']=''
    df2['greenby']=''
    df2['Volumea']=''

    for x in df.index:

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


        df2['a_Close'].loc[x]=1/4*(df['Open'].loc[x]+df2['High'].loc[x]+df2['Low'].loc[x]+df['Close'].loc[x])
        df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])
        df2['High'].loc[x]=df2['High'].loc[x]
        df2['Low'].loc[x]=df2['Low'].loc[x]
        df2['a_High'].loc[x]=max(df['High'].loc[x],df2['a_Open'].loc[x],df2['a_Close'].loc[x])
        df2['a_Low'].loc[x]=min(df['Low'].loc[x],df2['a_Open'].loc[x],df2['a_Close'].loc[x])
     #   df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])
        df2['HA'].loc[x]=df2['a_Close'].loc[x]-df2['a_Open'].loc[x]
    ##    df2['d']=df2['Date'].dt.day_name()
    #    print(df2)

    #   if df2['a_Close'].loc[x] > df2['a_Open'].loc[x]:
        if df2['HA'].loc[x] > 0:
            df2['direct'].loc[x]='HA_Green'
        elif df2['HA'].loc[x] < 0:
            df2['direct'].loc[x]='HA_Red'

        df['Volumea']=(df['Volume']-df['Volume'].shift(1))
    ############################ end of ha

    ##ddd=(df['Volume']-df['Volume'].shift(1))
    tt=pd.concat([df2['direct'],df2['HA'],df['Close'],(df['Close']-df['Close'].shift(1)),df['Volume'],df['Volumea'],
                  CCI,DX,WILLR,df['*'],CDLDOJI,CDLDOJISTAR,CDLDRAGONFLYDOJI,CDLEVENINGDOJISTAR,CDLGRAVESTONEDOJI,CDLHAMMER,CDLXSIDEGAP3METHODS,
                  df['*'],EMA_3,EMA_5,EMA_10,EMA_21,EMA_50,EMA_100,EMA_200],axis=1)

    tt.columns=['direct','HA','Close','Close_ch','Volume','Volumea','CCI','DX','WILLR',"*",'CDLDOJI','CDLDOJISTAR','CDLDRAGONFLYDOJI','CDLEVENINGDOJISTAR','CDLGRAVESTONEDOJI','CDLHAMMER','CDLXSIDEGAP3METHODS',
                '*','EMA_3','EMA_5','EMA_10','EMA_21','EMA_50','EMA_100','EMA_20']


    tt.reset_index(inplace=True)
##    tt=pd.DataFrame(tt)
##
##    for x in df.index:
##        if len(df['Volume'].loc[x])>9:
##            df['Volume'].loc[x]=str(np.float64(df['Volume'].loc[x])/np.float64(100000000))+' Billion'
##        elif len(df['Volume'].loc[x]) < 7:
##            df['Volume'].loc[x]=str(np.float64(df['Volume'].loc[x])/np.float64(1000000))+' Million'    
####        print(x,'   ',tt2['Close'].loc[x],'   ',tt2['Close'].loc[x]+tt2['Close'].loc[x])
##        
##          
####        tt['Close'].loc[x]=tt['Close'].loc[x]/5
####        np.float64(tt2['Close'].loc[x])==5
##        
####        tt['Volume'].loc[x]=np.float64(tt['Volume'].loc[x])/55555
##        
####        print(tt['Volume'])
####        tt['Volume'].loc[x]=numerize.numerize(np.float64(tt['Volume']).loc[x].item())
####        tt['Volume'].loc[x]=numerize.numerize(tt['Volume'].loc[x])
##    ##    tt['Volume'].loc[x]=numerize.numerize((tt['Volume'].iloc[x][1]))
####        if (tt['Volume'].loc[x]) > 4:
####        tt['Volume'].loc[x]=numerize.numerize(np.float(tt['Volume']).loc[x].item())
##    df.set_index('Datetime')
##
##
####    tt=pd.concat([df2['direct'],df2['HA'],df['Close'],(df['Close']-df['Close'].shift(1)),df['Volume'],df['Volumea'],CCI,DX,WILLR,df['*'],CDLDOJI,CDLDOJISTAR,CDLDRAGONFLYDOJI,CDLEVENINGDOJISTAR,CDLGRAVESTONEDOJI,CDLHAMMER,CDLXSIDEGAP3METHODS,
####                  df['*'],EMA_3,EMA_5,EMA_10,EMA_21,EMA_50,EMA_100,EMA_200],axis=1)
####
####    tt.columns=['direct','HA','Close','Close_ch','Volume','Volumea','CCI','DX','WILLR',"*",'CDLDOJI','CDLDOJISTAR','CDLDRAGONFLYDOJI','CDLEVENINGDOJISTAR','CDLGRAVESTONEDOJI','CDLHAMMER','CDLXSIDEGAP3METHODS',
####                '*','EMA_3','EMA_5','EMA_10','EMA_21','EMA_50','EMA_100','EMA_20']
####


##    print('CCI: ', tt)
##    print('Close: ', tt['Volume'])


      
    for x in tt.index:
    ##    print(tt['Volume'])
    ##    tt['Volume'].loc[x]=numerize.numerize(tt['Volume'].loc[x])
    ##    tt['Volume'].loc[x]=numerize.numerize((tt['Volume'].iloc[x][1]))
        tt['Volume'].loc[x]=numerize.numerize(np.float32(tt['Volume'].loc[x]).item())
    tt.set_index('Datetime')

    print(intervla,' Hourly CCI: ', tt)
    ##MA = ta.SMA(df['close'])
    ##print('MA: ',MA)    
days()
##hourly()
