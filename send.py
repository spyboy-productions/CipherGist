import os
import base64
import json
import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import requests

def encrypt_file(password):
    with open("config.txt", "rb") as f:
        data = f.read()

    key = base64.urlsafe_b64decode(password)
    aesgcm = AESGCM(key)
    nonce = secrets.token_bytes(12)
    ct = aesgcm.encrypt(nonce, data, None)

    encrypted_content = base64.b64encode(nonce + ct).decode()
    return encrypted_content

def upload_to_gist(content):
    token = None
    with open("config.txt", "r") as f:
        for line in f:
            if "GITHUB_TOKEN" in line:
                token = line.split("=", 1)[-1].strip().strip('"').strip("'")
                break

    if not token:
        print("❌ GITHUB_TOKEN not found in config.txt")
        return None

    headers = {
        "Authorization": f"token {token}"
    }

    data = {
        "description": "Encrypted config.txt",
        "public": True,
        "files": {
            "config.txt.enc": {
                "content": content
            }
        }
    }

    response = requests.post("https://api.github.com/gists", headers=headers, json=data)
    if response.status_code == 201:
        gist_url = response.json()["html_url"]
        print(f"✅ File uploaded: {gist_url}")
        return gist_url
    else:
        print(f"❌ Failed to upload: {response.status_code}")
        print(response.text)
        return None

if __name__ == "__main__":
    password_bytes = AESGCM.generate_key(bit_length=128)
    password = base64.urlsafe_b64encode(password_bytes).decode()

    print("🔒 Encrypting config.txt...")
    encrypted_content = encrypt_file(password)
    print("🔑 Generated password (share this securely):")
    print(password)

    print("🌐 Uploading encrypted content to GitHub Gist...")
    gist_link = upload_to_gist(encrypted_content)

    if gist_link:
        print("\n📝 Share this link and password with the receiver:")
        print(f"Gist: {gist_link}")
        print(f"Password: {password}")
