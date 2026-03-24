import requests
import time

def check_username(username):
    url = f"https://www.instagram.com/{username}/"
    
    response = requests.get(url)

    if response.status_code == 404:
        return "Available ✅"
    elif response.status_code == 200:
        return "Taken ❌"
    else:
        return "Error ⚠️"

def bulk_check(usernames):
    for username in usernames:
        status = check_username(username)
        print(f"{username} → {status}")
        time.sleep(2)  # avoid getting blocked

# Example usernames
usernames = input("Enter Instagram usernames (comma separated): ").split(",")
usernames = [u.strip() for u in usernames if u.strip()]

bulk_check(usernames)