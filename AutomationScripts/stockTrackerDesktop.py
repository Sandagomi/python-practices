import requests
import os
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# ---------------- LOAD API KEY ----------------
script_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(script_dir, '.env'))
API_KEY = os.getenv('APIKEY')

if not API_KEY:
    raise ValueError("❌ APIKEY not found in .env file")

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# ---------------- SEARCH COMPANY ----------------
def search_company():
    query = entry.get().strip()

    if not query:
        messagebox.showwarning("Warning", "Enter a company name")
        return

    url = "https://finnhub.io/api/v1/search"
    params = {"q": query, "token": API_KEY}

    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=5)
        data = response.json()
    except Exception as e:
        messagebox.showerror("Error", f"Search failed: {str(e)}")
        return

    listbox.delete(0, tk.END)

    results = data.get("result", [])

    valid_found = False

    for item in results:
        if (
            item.get("symbol") and
            item.get("description") and
            item.get("type") == "Common Stock"
        ):
            name = item["description"]
            symbol = item["symbol"]
            listbox.insert(tk.END, f"{name} ({symbol})")
            valid_found = True

        if listbox.size() >= 5:
            break

    if not valid_found:
        listbox.insert(tk.END, "No valid stocks found")


# ---------------- GET PRICE ----------------
def get_price():
    selected = listbox.get(tk.ACTIVE)

    if not selected or "No valid stocks" in selected:
        messagebox.showwarning("Warning", "Select a valid stock")
        return

    symbol = selected.split("(")[-1].split(")")[0].strip()

    url = "https://finnhub.io/api/v1/quote"
    params = {"symbol": symbol, "token": API_KEY}

    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=5)
        data = response.json()
    except Exception as e:
        messagebox.showerror("Error", f"Price fetch failed: {str(e)}")
        return

    price = data.get("c")
    prev = data.get("pc")

    if price is not None and price != 0:
        change = price - prev if prev else 0

        result_label.config(
            text=f"📊 {symbol} | Price: ${price} | Change: {round(change,2)}"
        )
    else:
        result_label.config(text=f"❌ No price data for {symbol}")


# ---------------- SHOW GRAPH ----------------
def show_graph():
    selected = listbox.get(tk.ACTIVE)

    if not selected or "No valid stocks" in selected:
        messagebox.showwarning("Warning", "Select a valid stock")
        return

    symbol = selected.split("(")[-1].split(")")[0].strip()

    end = int(datetime.now().timestamp())
    start = int((datetime.now() - timedelta(days=30)).timestamp())

    url = "https://finnhub.io/api/v1/stock/candle"
    params = {
        "symbol": symbol,
        "resolution": "D",
        "from": start,
        "to": end,
        "token": API_KEY
    }

    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=5)
        data = response.json()
    except Exception as e:
        messagebox.showerror("Error", f"Graph fetch failed: {str(e)}")
        return

    if data.get("s") != "ok":
        messagebox.showerror("Error", "No historical data available")
        return

    prices = data.get("c", [])
    timestamps = data.get("t", [])

    dates = [datetime.fromtimestamp(ts) for ts in timestamps]

    # 📊 Plot graph
    plt.figure()
    plt.plot(dates, prices)
    plt.title(f"{symbol} - Last 30 Days")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()


# ---------------- AUTO REFRESH ----------------
def auto_refresh():
    get_price()
    root.after(5000, auto_refresh)


# ---------------- UI ----------------
root = tk.Tk()
root.title("📈 Stock Tracker")
root.geometry("420x450")
root.resizable(False, False)

title = tk.Label(root, text="📈 Stock Tracker", font=("Arial", 16, "bold"))
title.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 11))
entry.pack(pady=5)

search_btn = tk.Button(root, text="Search", width=20, command=search_company)
search_btn.pack(pady=5)

listbox = tk.Listbox(root, width=50, height=6)
listbox.pack(pady=10)

price_btn = tk.Button(root, text="Get Price", width=20, command=get_price)
price_btn.pack(pady=5)

track_btn = tk.Button(root, text="Start Tracking", width=20, command=auto_refresh)
track_btn.pack(pady=5)

graph_btn = tk.Button(root, text="Show Graph", width=20, command=show_graph)
graph_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()