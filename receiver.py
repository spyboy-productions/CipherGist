import base64
import requests
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def download_encrypted_content(gist_url):
    gist_id = gist_url.strip().split("/")[-1]
    api_url = f"https://api.github.com/gists/{gist_id}"

    response = requests.get(api_url)

    if response.status_code == 200:
        files = response.json()["files"]
        if "config.txt.enc" in files:
            print("✅ Downloaded encrypted content.")
            return files["config.txt.enc"]["content"], gist_id
        else:
            print("❌ config.txt.enc not found in the Gist.")
            return None, None
    else:
        print("❌ Failed to fetch Gist.")
        return None, None

def decrypt_file(password, encrypted_content):
    key = base64.urlsafe_b64decode(password)
    data = base64.b64decode(encrypted_content)

    nonce = data[:12]
    ct = data[12:]

    aesgcm = AESGCM(key)
    try:
        plaintext = aesgcm.decrypt(nonce, ct, None)
        with open("config.txt", "wb") as f:
            f.write(plaintext)
        print("✅ File decrypted and saved as config.txt")
        return plaintext.decode()
    except Exception as e:
        print("❌ Decryption failed!")
        print(e)
        return None

def extract_token(config_data):
    for line in config_data.splitlines():
        if line.startswith("GITHUB_TOKEN="):
            return line.split("=", 1)[1].strip()
    return None

def delete_gist(gist_id, token):
    api_url = f"https://api.github.com/gists/{gist_id}"
    headers = {"Authorization": f"token {token}"}
    response = requests.delete(api_url, headers=headers)

    if response.status_code == 204:
        print("🗑️ Gist deleted successfully.")
    else:
        print("⚠️ Failed to delete Gist.")
        print(response.status_code, response.text)

if __name__ == "__main__":
    gist_link = input("🔗 Enter Gist link: ").strip()
    password = input("🔑 Enter password: ").strip()

    print("⬇️ Downloading encrypted file...")
    enc_content, gist_id = download_encrypted_content(gist_link)

    if enc_content:
        print("🔓 Decrypting file...")
        config_text = decrypt_file(password, enc_content)

        if config_text:
            token = extract_token(config_text)
            if token:
                print("🧹 Deleting Gist using token from config.txt...")
                delete_gist(gist_id, token)
            else:
                print("⚠️ GITHUB_TOKEN not found in config.txt")
