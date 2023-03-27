



import pandas as pd
df_orig = pd.read_json(‘tesla_tweets.json’, encoding=’utf-8')
df = df_orig.copy()
df = df[['timestamp', 'text', 'username']]
df.set_index(pd.to_datetime(df['timestamp']), inplace=True)
df.drop(columns='timestamp', inplace=True)
df.drop_duplicates(subset=['text'], keep=False, inplace=True)




















##import ssl
##
##try:
##    _create_unverified_https_context = ssl._create_unverified_context
##except AttributeError:
##    pass
##else:
##    ssl._create_default_https_context = _create_unverified_https_context
##
##
##
##import pandas as pd
##import matplotlib.pyplot as plt
##import datetime as dt
##import nltk
##from nltk.sentiment.vader import SentimentIntensityAnalyzer
##from GoogleNews import GoogleNews
##from newspaper import Article
##from newspaper import Config
####from wordcloud import WordCloud, STOPWORDS
##
##nltk.download('vader_lexicon') #required for Sentiment Analysis
##now = dt.date.today()
##now = now.strftime('%m-%d-%Y')
##yesterday = dt.date.today() - dt.timedelta(days = 1)
##yesterday = yesterday.strftime('%m-%d-%Y')
##
##nltk.download('punkt')
##user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'
##config = Config()
##config.browser_user_agent = user_agent
##config.request_timeout = 10
##
##company_name = input("Please provide the name of the Company or a Ticker: ")
###As long as the company name is valid, not empty...
##if company_name != '':
##    print(f'Searching for and analyzing {company_name}, Please be patient, it might take a while...')
##
##    #Extract News with Google News
##    googlenews = GoogleNews(start=yesterday,end=now)
##    googlenews.search(company_name)
##    result = googlenews.result()
##    #store the results
##    df = pd.DataFrame(result)
##    print(df)


##try:
    list =[] #creating an empty list 
    for i in df.index:
        dict = {} #creating an empty dictionary to append an article in every single iteration
        article = Article(df['link'][i],config=config) #providing the link
##        try:
##          article.download() #downloading the article 
##          article.parse() #parsing the article
##          article.nlp() #performing natural language processing (nlp)
##        except:
##            pass 
##        #storing results in our empty dictionary
        dict['Date']=df['date'][i] 
        dict['Media']=df['media'][i]
        dict['Title']=article.title
        dict['Article']=article.text
        dict['Summary']=article.summary
        dict['Key_words']=article.keywords
        list.append(dict)
        check_empty = not any(list)
        # print(check_empty)
        if check_empty == False:
          news_df=pd.DataFrame(list) #creating dataframe
        print(news_df)
