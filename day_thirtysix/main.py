import requests
from datetime import datetime, timedelta
# from bulksms import SmsApi, SmsApiException

STOCK_NAME = "TSLA" 
COMPANY_NAME = "Tesla Inc" 
STOCK_ENDPOINT = "https://www.alphavantage.co/query" 
NEWS_ENDPOINT = "https://newsapi.org/v2/everything" ## STEP 1: Use https://www.alphavantage.co/documentation/#daily # When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News"). #TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()] import requests from datetime import datetime, timedelta API_KEY = "KUFQ0CSNN0C4B9CE" params = { "function": "TIME_SERIES_DAILY", "symbol": STOCK_NAME, "apikey": API_KEY } response = requests.get(STOCK_ENDPOINT, params=params) data = response.json()["Time Series (Daily)"] yesterday_date = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d') yesterday_close = float(data[yesterday_date]["4. close"]) #TODO 2. - Get the day before yesterday's closing stock price day_before_yesterday_date = (datetime.now() - timedelta(2)).strftime('%Y-%m-%d') day_before_yesterday_close = float(data[day_before_yesterday_date]["4. close"]) #TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp difference = abs(yesterday_close - day_before_yesterday_close) #TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday. percentage_difference = (difference / day_before_yesterday_close) * 100 #TODO 5. - If TODO4 percentage is greater than 5 then print("Get News"). if percentage_difference > 5: print("Get News") ## STEP 2: https://newsapi.org/ # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. #TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME. news_params = { "qInTitle": COMPANY_NAME, "apiKey": "30dadb49fb8041cba25c841c48924aa4" } news_response = requests.get(NEWS_ENDPOINT, params=news_params) articles = news_response.json()["articles"] #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation three_articles = articles[:3] ## STEP 3: Use bulksms/quickstart/python # Send a separate message with each article's title and description to your phone number. from bulksms import SmsApi, SmsApiException sms_api = SmsApi(username='tangel', password='20603261Tsa') for article in three_articles: title = article['title'] description = article['description'] message = f"Headline: {title}\nBrief: {description}" try: response = sms_api.send_message(to='your_phone_number', message=message) print(f"Message sent: {response}") except SmsApiException as e: print(f"Failed to send message: {e}") #to send a separate message with each article's title and description to your phone number. #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension. formatted_articles = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in three_articles] #TODO 9. - Send each article as a separate message via Bulksms. for article in formatted_articles: try: response = sms_api.send_message(to='+27812593341', message=article) print(f"Message sent: {response}") except SmsApiException as e: print(f"Failed to send message: {e}") #Optional TODO: Format the message like this: """ TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash. or "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash. """

STOCK_API_KEY = "KUFQ0CSNN0C4B9CE"
NEWS_API_KEY = "30dadb49fb8041cba25c841c48924aa4"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily # When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()] import requests from datetime import datetime, timedelta
stock_params = {
      "function": "TIME_SERIES_DAILY",
      "symbol": STOCK_NAME,
      "apikey": STOCK_API_KEY,
  }
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
print(day_before_yesterday_closing_price)    

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# print(difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percentage = round((difference / yesterday_closing_price) * 100)
# print(diff_percentage)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percentage > 5:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    # print(articles)
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{difference}%\nHeadline: {article['title']}\nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)

#TODO 9. - Send each article as a separate message via Bulksms.
    BULKSMS_URL = "https://api.bulksms.com/v1/messages"
    BULKSMS_USER = "tangel"
    BULKSMS_PASS = "20603261Tsa"

    for article in formatted_articles:
        sms_payload = {
            "to": "+27812593341",
            "body": article
        }
        resp = requests.post(
            BULKSMS_URL,
            auth=(BULKSMS_USER, BULKSMS_PASS),
            json=sms_payload
        )
        print("SMS response:", resp.json())




# ................AI.....................
# import requests
# from datetime import datetime

# # --- Config ---
# STOCK_NAME = "TSLA"
# COMPANY_NAME = "Tesla Inc"

# STOCK_ENDPOINT = "https://www.alphavantage.co/query"
# NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# ALPHA_API_KEY = "KUFQ0CSNN0C4B9CE"   # Replace with your Alpha Vantage key
# NEWS_API_KEY = "30dadb49fb8041cba25c841c48924aa4"  # Replace with your NewsAPI key

# # --- STEP 1: Get stock data ---
# params = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK_NAME,
#     "apikey": ALPHA_API_KEY
# }

# response = requests.get(STOCK_ENDPOINT, params=params)
# data = response.json()["Time Series (Daily)"]

# # Get the two most recent trading days
# dates = sorted(data.keys(), reverse=True)[:2]
# yesterday_date, day_before_date = dates

# yesterday_close = float(data[yesterday_date]["4. close"])
# day_before_close = float(data[day_before_date]["4. close"])

# # --- STEP 2: Calculate difference ---
# difference = yesterday_close - day_before_close
# percentage_difference = (abs(difference) / day_before_close) * 100

# # Format arrow
# arrow = "🔺" if difference > 0 else "🔻"

# print(f"{STOCK_NAME}: {arrow}{round(percentage_difference,2)}%")

# # --- STEP 3: If change > 5%, fetch news ---
# if percentage_difference > 5:
#     print("Get News...")

#     news_params = {
#         "qInTitle": COMPANY_NAME,
#         "apiKey": NEWS_API_KEY,
#         "language": "en",
#         "sortBy": "publishedAt",
#         "pageSize": 3
#     }

#     news_response = requests.get(NEWS_ENDPOINT, params=news_params)
#     articles = news_response.json()["articles"]

#     # Format articles
#     formatted_articles = [
#         f"{STOCK_NAME}: {arrow}{round(percentage_difference,2)}%\n"
#         f"Headline: {article['title']}\n"
#         f"Brief: {article['description']}"
#         for article in articles
#     ]

#     # --- STEP 4: Send SMS via BulkSMS ---
#     from bulksms import SmsApi, SmsApiException
#     sms_api = SmsApi(username='tangel', password='20603261Tsa')

#     for article in formatted_articles:
#         try:
#             response = sms_api.send_message(to='+27812593341', message=article)
#             print(f"Message sent: {response}")
#         except SmsApiException as e:
#             print(f"Failed to send message: {e}")
