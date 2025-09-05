import os
import time

# Clear the terminal
os.system('clear')

# Updated ASCII Art for the title
banner = """
: 
_     ____  __   ___ _____ 
\ \   / / _ \|  _ \ / __|  ___|
 \ \_/ / |  | | |_) | (__ | |_   
  \   /| |  | |  _ < \__ \|  _|  
   | | | |_| | |_) |__) | |___ 
   |_|  \___/|__/|___/|_____|

  
:        By The Kali User's     
 
"""
print(banner)

# Get target phone number
print("Enter Targeted Number ", end=": ")
phone_number = input()

# Simulate steps with messages
steps = [
    " Scanning {phone_number}: ",
    " Exploiting To {phone_number}: ",
    " Bypass Verify WhatsApp: ",
    " Success Bypass: ",
    " Get Verify Code: ",
]

for step in steps:
    print(step.format(phone_number=phone_number))
    time.sleep(2)

# Set the verification code
verify_code = "65568"  # Fixed verification code
print(f" Verify Code : {verify_code}: ", end="")
time.sleep(1)

print(" CamPhish/YsrWhatsApp: ", end=": ") # Simulate command prompt
# End of script
