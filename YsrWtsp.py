#```python
import os
import time
import getpass
import random
from datetime import datetime

#--- Login System ---
username = "yasir"
password = "khan"

print("==== LOGIN REQUIRED ====")
input_user = input("Username: ")
input_pass = getpass.getpass("Password: ")  # Hides password input

if input_user != username or input_pass != password:
    print("Access Denied ❌")
    exit()

#Clear the terminal
os.system('clear')

#ASCII Art Banner
banner = """
_     _  _   _ _ 
\\ \\   / / _ \\|  _ \\ / |  _|
 \\ \\/ / |  | | |) | (_ | |   
  \\   /| |  | |  _ < \\__ \\|  _|  
   | | | || | |) |) | |_ 
   ||  \\/|/|/||

   By The Kali User's  
       Author   : Yasir Muhammad   
   Whatsapp  : +923260907808
    GitHub   : https://github.com/yasirkhaan7
    Tiktok   : https://www.tiktok.com/@yasir__.__
    Instagram: https://www.instagram.com/yasir_khaan7/
    Facebook : https://web.facebook.com/yasir.khaan360
    Facebook : https://web.facebook.com/profile.php?id=61579898902452
    YouTube  : https://www.youtube.com/c/TheKaliUsers
    Donate (Habib Bank Limited) HBL : (IBAN) PK68HABB0001987902061799
    Version  : 1.0
    Date     : 2025-09-06
    Note     : This is for educational purposes only.
    Use it responsibly.
    Legal    : TheKaliUsers is not responsible for any misuse of this tool.
    Follow   : @TheKaliUser's on all platforms
    Enjoy   : Ethical Hacking & Cyber Security Learning!
"""
print(banner)

#Get target phone number
phone_number = input("Enter Targeted Number: ")

#Simulated steps
steps = [
    f"Scanning {phone_number}...",
    f"Exploiting {phone_number}...",
    "Bypassing WhatsApp verification...",
    "Bypass successful...",
    "Retrieving OTP..."
]

for step in steps:
    print(step)
    time.sleep(2)

#Generate random 6-digit OTP
verify_code = random.randint(100000, 999999)
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Verify Code: {verify_code}  |  Time: {now}")
time.sleep(1)
print("OTP Retrieved Successfully ✅")
with open("otp_log.txt", "a") as log:
    log.write(f"{phone_number} | OTP: {verify_code} | Time: {now}\n")

#python
print("\n--- Security Awareness ---")
print("⚠️ Never share your OTP with anyone.")
print("⚠️ Use strong, unique passwords.")
print("⚠️ Enable two-factor authentication (2FA) wherever possible.")
print("⚠️ Be cautious of phishing attempts.")
print("Stay safe online! 🚀")

# Optional: Add a phishing simulation warning before running

#python
print("""
** WARNING: This tool is for educational purposes only. **
Do not use it for illegal activities.
This simulates how attackers try to bypass OTPs to promote awareness.
""")
time.sleep(3)
