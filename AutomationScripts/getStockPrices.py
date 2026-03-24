import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('APIKEY')

# 🔍 Step 1: Search company name → symbol
def search_company(name):
    url = "https://finnhub.io/api/v1/search"
    
    params = {
        "q": name,
        "token": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    results = data.get("result", [])

    companies = []
    for item in results:
        if item.get("symbol") and item.get("description"):
            companies.append({
                "symbol": item["symbol"],
                "name": item["description"]
            })

    return companies


# 📈 Step 2: Get stock price
def get_stock_price(symbol):
    url = "https://finnhub.io/api/v1/quote"
    
    params = {
        "symbol": symbol,
        "token": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    price = data.get("c")
    prev_close = data.get("pc")

    if price:
        change = price - prev_close
        return price, change
    return None, None


# 🔍 User input (company name)
query = input("Enter company name: ")

companies = search_company(query)

if not companies:
    print("No companies found.")
    exit()

# Show top 5 matches
print("\nSelect a company:")
for i, c in enumerate(companies[:5]):
    print(f"{i+1}. {c['name']} ({c['symbol']})")

choice = int(input("\nEnter choice (1-5): ")) - 1
selected = companies[choice]

# 📈 Fetch price
price, change = get_stock_price(selected["symbol"])

if price:
    print(f"\n📊 {selected['name']} ({selected['symbol']})")
    print(f"Price: ${price}")

    if change > 0:
        print(f"Change: +{round(change,2)} 🔺")
    else:
        print(f"Change: {round(change,2)} 🔻")
else:
    print("Could not fetch price.")