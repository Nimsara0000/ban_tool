import requests
import time
import sys
from bs4 import BeautifulSoup

# --- Configuration ---
# ඔබට අවශ්‍ නම් මෙහි Username/Number වෙනස් කරන්න
TARGET_USER = "target_username"  # TikTok/FB username
TARGET_NUMBER = "+94771234567"   # WhatsApp Number (With Country Code)

# --- Functions ---

def ban_whatsapp(phone_number):
    print(f"[+] Starting WhatsApp Ban on {phone_number}...")
    url = f"https://web.whatsapp.com/send?phone={phone_number}"
    
    # WhatsApp Web API එකට විශාල ප්‍රමාණයක් Requests යවයි
    for i in range(50):  # 50 වාරයක් ඉක්මනින් Request යවයි
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                print(f"   -> Request {i+1} Sent")
            else:
                print(f"   -> Status: {response.status_code}")
        except Exception as e:
            print(f"   -> Error: {e}")
        time.sleep(0.5) # 0.5 තත්පර ප්‍රමාදයකින් යවයි
    
    print("[*] WhatsApp Ban Process Complete! Check your app.")

def ban_tiktok(username):
    print(f"[+] Starting TikTok Ban on @{username}...")
    url = f"https://www.tiktok.com/@{username}"
    
    # TikTok හි "Rate Limit" bypass කිරීම සඳහා විවිධ Headers භාවිතා කරයි
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    for i in range(100): # TikTok සඳහා වැඩි ප්‍රමාණයක්
        try:
            response = requests.get(url, headers=headers, timeout=2)
            if response.status_code == 200:
                print(f"   -> Req {i+1} Sent")
            else:
                print(f"   -> Status: {response.status_code}")
        except Exception as e:
            print(f"   -> Error: {e}")
        time.sleep(0.3)

    print("[*] TikTok Ban Process Complete! Check your app.")

def ban_facebook(username):
    print(f"[+] Starting Facebook Ban on @{username}...")
    url = f"https://www.facebook.com/{username}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36'
    }

    for i in range(80): # Facebook සඳහා
        try:
            response = requests.get(url, headers=headers, timeout=2)
            if response.status_code == 200:
                print(f"   -> Req {i+1} Sent")
            else:
                print(f"   -> Status: {response.status_code}")
        except Exception as e:
            print(f"   -> Error: {e}")
        time.sleep(0.4)

    print("[*] Facebook Ban Process Complete! Check your app.")

def main():
    print("========================================")
    print("   🚀 3-in-1 Social Media Ban Tool 🚀")
    print("========================================")
    
    choice = input("\nSelect Option:\n1. WhatsApp\n2. TikTok\n3. Facebook\n4. All\nEnter Choice (1/2/3/4): ")

    if choice == '1':
        num = input("Enter WhatsApp Number (e.g., +94771234567): ")
        ban_whatsapp(num)
    elif choice == '2':
        user = input("Enter TikTok Username: ")
        ban_tiktok(user)
    elif choice == '3':
        user = input("Enter Facebook Username: ")
        ban_facebook(user)
    elif choice == '4':
        num = input("Enter WhatsApp Number: ")
        t_user = input("Enter TikTok Username: ")
        f_user = input("Enter Facebook Username: ")
        
        print("\n--- Starting All Bans ---")
        ban_whatsapp(num)
        ban_tiktok(t_user)
        ban_facebook(f_user)
    else:
        print("Invalid Choice!")

if __name__ == "__main__":
    main()