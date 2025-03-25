import os
import time
import json
import requests
import nacl.public
import nacl.signing
import nacl.encoding
import threading
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)  # Auto-reset colors

CONFIG_FILE = "config.txt"

# Load config file
def load_config():
    config = {}
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if "=" in line:
                    key, value = line.split("=", 1)
                    config[key.strip()] = value.strip()
    return config

# Ensure keys exist
config = load_config()
required_keys = ["SIGNING_PRIVATE", "SIGNING_PUBLIC", "ENCRYPTION_PRIVATE", "ENCRYPTION_PUBLIC"]

if not all(key in config for key in required_keys):
    print("🔍 Keys missing! Generating new keys using make_keys.py...")
    os.system("python make_keys.py")
    config = load_config()  # Reload after generation

# Ensure GitHub Token & Gist ID exist
if "GIST_ID" not in config or "GITHUB_TOKEN" not in config:
    print("\n🔑 Enter your GitHub Gist ID and Token (stored in config.txt)")
    config["GIST_ID"] = input("📜 Gist ID: ").strip()
    config["GITHUB_TOKEN"] = input("🔐 GitHub Token: ").strip()
    with open(CONFIG_FILE, "a") as file:
        file.write(f"\nGIST_ID={config['GIST_ID']}")
        file.write(f"\nGITHUB_TOKEN={config['GITHUB_TOKEN']}\n")

# Load credentials
GIST_ID = config["GIST_ID"]
GITHUB_TOKEN = config["GITHUB_TOKEN"]

# GitHub API Setup
GIST_URL = f"https://api.github.com/gists/{GIST_ID}"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}

# Validate GitHub Token
response = requests.get("https://api.github.com/user", headers=HEADERS)
if response.status_code != 200:
    print("❌ Invalid GitHub Token! Please check your config.txt.")
    exit(1)

# Validate Gist ID
response = requests.get(GIST_URL, headers=HEADERS)
if response.status_code != 200:
    print("❌ Invalid or inaccessible Gist ID! Please check your config.txt.")
    exit(1)

# Convert hex keys to actual keys
signing_private = nacl.signing.SigningKey(bytes.fromhex(config["SIGNING_PRIVATE"]))
encryption_private = nacl.public.PrivateKey(bytes.fromhex(config["ENCRYPTION_PRIVATE"]))
encryption_public = nacl.public.PublicKey(bytes.fromhex(config["ENCRYPTION_PUBLIC"]))

def get_latest_message():
    response = requests.get(GIST_URL, headers=HEADERS)
    if response.status_code == 200:
        files = json.loads(response.text).get("files", {})
        if "chat.txt" in files:
            return files["chat.txt"]["content"]
    return None

def update_gist(message):
    data = {"files": {"chat.txt": {"content": message}}}
    response = requests.patch(GIST_URL, headers=HEADERS, json=data)
    return response.status_code == 200

def encrypt_message(message, receiver_public_key):
    sealed_box = nacl.public.SealedBox(receiver_public_key)
    return sealed_box.encrypt(message.encode(), encoder=nacl.encoding.Base64Encoder).decode()

def decrypt_message(encrypted_message):
    try:
        sealed_box = nacl.public.SealedBox(encryption_private)
        return sealed_box.decrypt(encrypted_message.encode(), encoder=nacl.encoding.Base64Encoder).decode()
    except Exception as e:
        return f"❌ Decryption error: {e}"

# Track last sent message
last_sent_message = None  

def format_message(sender, message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    if sender == "You":
        return f"{Fore.YELLOW}{timestamp} ✅"
    else:
        return f"{Fore.YELLOW}{timestamp} {Fore.BLUE}Someone: {Fore.RESET}{message}"

def send_message():
    global last_sent_message
    while True:
        message = input(f"{Fore.CYAN}\n📪📨 {Style.RESET_ALL}")
        encrypted = encrypt_message(message, encryption_public)
        
        if update_gist(encrypted):
            last_sent_message = encrypted
            print(format_message("You", message))
        else:
            print(f"{Fore.RED}❌ Failed to send message.")

def fetch_messages():
    last_message = None
    while True:
        time.sleep(3)
        encrypted_message = get_latest_message()

        if encrypted_message and encrypted_message != last_message and encrypted_message != last_sent_message:
            last_message = encrypted_message
            decrypted_message = decrypt_message(encrypted_message)
            print("\n" + format_message("Someone", decrypted_message))

if __name__ == "__main__":
    print(f"\n{Fore.CYAN}🪪 Share your config.txt with your friend or use theirs to start chatting.")
    print(f"{Fore.GREEN}🔐 Secure Messenger Started...")

    fetch_thread = threading.Thread(target=fetch_messages, daemon=True)
    fetch_thread.start()
    
    send_message()
