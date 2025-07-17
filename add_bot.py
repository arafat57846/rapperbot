import json

bot_username = input("🔁 Enter bot username (without @): ")
refer_code = input("🎯 Enter new refer code: ")

with open("config.json", "w") as f:
    json.dump({
        "bot_username": bot_username,
        "refer_code": refer_code
    }, f, indent=2)

print("✅ Config updated.")
