from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os

api_id = 28811286  # Replace with your own API ID
api_hash = '0ed0f922a0796bca4ffd46813ddb672a'  # Replace with your own API HASH

# Make sure the sessions directory exists
if not os.path.exists("sessions"):
    os.makedirs("sessions")

# Get phone number input
phone = input("📱 Enter phone number (with country code, like +8801XXXXXX): ").strip()

# Save phone number to saved_phones.txt
with open("saved_phones.txt", "a") as f:
    f.write(phone + "\n")

# Start session
client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    code = input("📩 Enter the code you received: ")
    client.sign_in(phone, code)

print("✅ Login successful.")
client.disconnect()
