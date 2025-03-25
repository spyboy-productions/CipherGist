import os
import nacl.signing
import nacl.public

CONFIG_FILE = "config.txt"

# Load config file safely
def load_config():
    config = {}
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if "=" in line:  # Ensure the line contains "="
                    key, value = line.split("=", 1)
                    config[key.strip()] = value.strip()
    return config

def generate_keys():
    print("🔑 Generating new keys...")

    # Generate Signing Key Pair (Ed25519)
    signing_key = nacl.signing.SigningKey.generate()
    verify_key = signing_key.verify_key

    # Generate Encryption Key Pair (X25519)
    private_key = nacl.public.PrivateKey.generate()
    public_key = private_key.public_key

    # Convert keys to hex
    signing_private_hex = signing_key.encode().hex()
    signing_public_hex = verify_key.encode().hex()
    encryption_private_hex = private_key.encode().hex()
    encryption_public_hex = public_key.encode().hex()

    # Save keys to config.txt
    with open(CONFIG_FILE, "a") as f:
        f.write(f"\nSIGNING_PRIVATE={signing_private_hex}")
        f.write(f"\nSIGNING_PUBLIC={signing_public_hex}")
        f.write(f"\nENCRYPTION_PRIVATE={encryption_private_hex}")
        f.write(f"\nENCRYPTION_PUBLIC={encryption_public_hex}\n")

    print("✅ Keys generated and saved in config.txt!")

# Run key generation only if keys are missing
config = load_config()
required_keys = ["SIGNING_PRIVATE", "SIGNING_PUBLIC", "ENCRYPTION_PRIVATE", "ENCRYPTION_PUBLIC"]

if not all(key in config for key in required_keys):
    generate_keys()
else:
    print("✅ Keys already exist in config.txt")
