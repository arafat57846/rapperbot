from telethon.sync import TelegramClient

api_id = 28811286
api_hash = "0ed0f922a0796bca4ffd46813ddb672a"

phone = input("📱 Enter phone number (with country code, like +8801XXXXXX): ")

client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    code = input("📩 Enter the code you received: ")
    try:
        client.sign_in(phone, code)
        print("✅ Login successful.")
    except Exception as e:
        print("❌ Failed to login:", e)
else:
    print("✅ Already logged in.")
client.disconnect()
