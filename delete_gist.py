import requests

def extract_token(config_path="config.txt"):
    try:
        with open(config_path, "r") as f:
            for line in f:
                if line.startswith("GITHUB_TOKEN="):
                    return line.split("=", 1)[1].strip()
        print("❌ GITHUB_TOKEN not found in config.txt")
        return None
    except FileNotFoundError:
        print("❌ config.txt not found!")
        return None

def delete_gist(gist_id, token):
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {"Authorization": f"token {token}"}
    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print("✅ Gist deleted successfully.")
    else:
        print("❌ Failed to delete gist.")
        print(response.status_code, response.text)

if __name__ == "__main__":
    gist_id = input("🆔 Enter Gist ID to delete: ").strip()
    token = extract_token()

    if token:
        delete_gist(gist_id, token)
