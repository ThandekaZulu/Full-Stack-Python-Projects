# 1. Stock price 9 = $900 & 10 = $1000
# 2. News API get 3 articles related to stock
# 3. Send sms with article titles & brief description
import requests

# --- Alpha Vantage setup ---
API_KEY = "KUFQ0CSNN0C4B9CE"
url = "https://www.alphavantage.co/query"

# --- Request daily forex data for USD/GBP ---
params = {
    "function": "FX_DAILY",
    "from_symbol": "USD",
    "to_symbol": "GBP",
    "apikey": API_KEY
}

response = requests.get(url, params=params)
data = response.json()

# --- Extract time series data ---
time_series = data["Time Series FX (Daily)"]

# Get the two most recent days
dates = sorted(time_series.keys(), reverse=True)[:2]
latest_date, previous_date = dates

latest_close = float(time_series[latest_date]["4. close"])
previous_close = float(time_series[previous_date]["4. close"])

# --- Compare prices ---
if latest_close > previous_close:
    trend = "increased 📈"
elif latest_close < previous_close:
    trend = "decreased 📉"
else:
    trend = "remained the same ➖"

# --- Determine currency strength ---
def currency_strength(rate):
    """
    If USD/GBP > 1 → USD stronger (1 USD > 1 GBP).
    If USD/GBP < 1 → GBP stronger (1 USD < 1 GBP).
    """
    if rate > 1:
        return "USD is stronger 💪"
    elif rate < 1:
        return "GBP is stronger 💪"
    else:
        return "USD and GBP are equal ⚖️"

previous_strength = currency_strength(previous_close)
latest_strength = currency_strength(latest_close)

# --- Report ---
print(f"USD/GBP comparison:")
print(f"- {previous_date}: {previous_close} ({previous_strength})")
print(f"- {latest_date}: {latest_close} ({latest_strength})")
print(f"Result: The USD/GBP rate has {trend} from {previous_date} to {latest_date}.")

# ...........NEWS API PART...........
import requests

# --- NewsAPI setup ---
API_KEY = "30dadb49fb8041cba25c841c48924aa4"  # Replace with your key from https://newsapi.org
url = "https://newsapi.org/v2/everything"

# --- Search for forex news related to USD and GBP ---
params = {
    "q": "USD GBP forex OR currency exchange OR dollar OR pound",
    "language": "en",
    "sortBy": "publishedAt",
    "apiKey": API_KEY,
    "pageSize": 5   # limit to 5 latest articles
}

response = requests.get(url, params=params)
data = response.json()

# --- Display headlines ---
if data["status"] == "ok":
    articles = data["articles"]
    print("Latest Forex News (USD/GBP):\n")
    for article in articles:
        print(f"- {article['title']} ({article['source']['name']})")
        print(f"  Published: {article['publishedAt']}")
        print(f"  URL: {article['url']}\n")
else:
    print("Error fetching news:", data)
