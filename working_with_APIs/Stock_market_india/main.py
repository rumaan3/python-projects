import requests
import math
from datetime import datetime, timedelta

# from twilio.rest.api.v2010.account.usage.record import YesterdayList

# from working_with_APIs.Trivia_quiz.data import response

STOCK_NAME = "500400"
COMPANY_NAME = "Nvidia"

today = datetime.now()
yesterday = (today-timedelta(days=1)).date()
today = str(today)
yesterday = str(yesterday)

# STOCK_ENDPOINT = "https://www.alphavantage.co/query"
# NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

api_key = "D5G6WIHR3ZB4SSA7"
api_news_key = "c7103c71b795443dac26cb887a2c6cab"
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={api_key}'

news_params = {
    "apiKey": api_news_key,
    "q": COMPANY_NAME,
}
url_news = f"https://newsapi.org/v2/top-headlines?"

news_data = requests.get(url_news,params=news_params)


# today = "2024-11-25"
# yesterday = "2024-11-22"

response = requests.get(url)
data = response.json()
close_data_today=data["Time Series (Daily)"][today]["4. close"]
close_data_yesterday=data["Time Series (Daily)"][yesterday]["4. close"]

close_data_today = round(float(close_data_today),2)
close_data_yesterday = round(float(close_data_yesterday),2)

stock_difference=round(float(float(close_data_today)-float(close_data_yesterday)),2)
stock_difference = abs(stock_difference)

percentage = (stock_difference/close_data_yesterday)*100










    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

