from telethon.sync import TelegramClient
import json
import os

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

bot_username = config["bot_username"]
refer_code = config["refer_code"]

api_id = 28811286
api_hash = "0ed0f922a0796bca4ffd46813ddb672a"

sessions_dir = "sessions"
sessions = [f for f in os.listdir(sessions_dir) if f.endswith(".session")]

if not sessions:
    print("❌ No sessions found. Please login with add_session.py first.")
    exit()

for session_file in sessions:
    session_name = session_file.replace(".session", "")
    print(f"🤖 Using session: {session_name}")
    try:
        client = TelegramClient(f"{sessions_dir}/{session_name}", api_id, api_hash)
        client.start()
        client.send_message(bot_username, f"/start {refer_code}")
        print(f"✅ Sent refer from {session_name}")
        client.disconnect()
    except Exception as e:
        print(f"❌ Failed for {session_name}: {e}")
