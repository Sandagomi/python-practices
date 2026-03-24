import requests
import time

def check_username_Insta(usernamesInstagram):
    url = f"https://www.instagram.com/{usernamesInstagram}/"
    
    response = requests.get(url)

    if response.status_code == 404:
        return "Available ✅"
    elif response.status_code == 200:
        return "Taken ❌"
    else:
        return "Error ⚠️"
    
def check_username_Tiktok(usernameTiktok):
    url1 = f"https://www.tiktok.com/{usernameTiktok}/"
    
    response = requests.get(url1)

    if response.status_code == 404:
        return "Available ✅"
    elif response.status_code == 200:
        return "Taken ❌"
    else:
        return "Error ⚠️"

def bulk_check_Insta(usernamesInstagram):
    for username in usernamesInstagram:
        status = check_username_Insta(username)
        print(f"{username} → {status}")
        time.sleep(2)  # avoid getting blocked
        
def bulk_check_Tiktok(usernameTiktok):
    for username in usernameTiktok:
        status = check_username_Tiktok(username)
        print(f"{username} → {status}")
        time.sleep(2)  # avoid getting blocked

# Example usernames
usernamesInstagram = input("Enter Instagram usernames (comma separated): ").split(",")
usernamesTiktok = input("Enter TikTok usernames (comma separated): ").split(",")

usernamesInstagram = [u.strip() for u in usernamesInstagram if u.strip()]
usernamesTiktok = [u.strip() for u in usernamesTiktok if u.strip()]

bulk_check_Insta(usernamesInstagram)
bulk_check_Tiktok(usernamesTiktok)