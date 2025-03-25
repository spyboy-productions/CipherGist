## 🛡️ CipherGist - Secure Encrypted Messenger  
**End-to-End Encrypted Messaging via GitHub Gists**

CipherGist is a lightweight, secure, and open-source encrypted messenger that enables private communication using GitHub Gists as the backend. It leverages **NaCl (libsodium)** for state-of-the-art encryption, ensuring that only the intended recipient can decrypt your messages. No centralized servers, no metadata tracking—just pure encrypted messaging.

---

## ✨ Features  
✅ **End-to-End Encryption** – Uses **Ed25519 (signing)** and **X25519 (encryption)** for secure communication.  
✅ **No Central Server** – Messages are stored and exchanged via GitHub Gists.  
✅ **Self-Destructing Keys** – Private keys are never shared or stored remotely.  
✅ **Lightweight & Fast** – Runs in a terminal, with minimal dependencies.  
✅ **Cross-Platform** – Works on **Windows, macOS, and Linux**.  
✅ **Fully Open-Source** – Code transparency ensures security.  

---

## 🔥 What Makes CipherGist Unique?  
🔹 Unlike traditional messengers (WhatsApp, Signal), **CipherGist does not use a central server**.  
🔹 No phone number, email, or identity required—**just a GitHub account**.  
🔹 Messages are **not stored permanently**—once deleted from Gist, they are gone forever.  
🔹 **No third-party tracking**—GitHub itself can't read your encrypted messages.  

---

## 🛠️ Installation & Setup  

### 1️⃣ Install Dependencies  
Ensure you have **Python 3** installed. Then, install the required libraries:  

```sh
pip install pynacl requests colorama
```

### 2️⃣ Create a GitHub Account  
Go to [GitHub](https://github.com/) and create an account if you don’t have one.

### 3️⃣ Get a GitHub Token  
1. Visit: [GitHub Developer Settings](https://github.com/settings/tokens)  
2. Click **"Generate new token" (classic)**  
3. Select **"Gist"** permission  
4. Copy and save your **GitHub Token** (you won’t see it again!)

### 4️⃣ Create a Gist  
1. Go to: [GitHub Gists](https://gist.github.com/)  
2. Click **"New Gist"**  
3. Name it **chat.txt** (keep it public or secret)  
4. Click **"Create secret gist"**  
5. Copy the **Gist ID** (last part of the URL: `https://gist.github.com/your-username/xxxxxxxxxx`)

### 5️⃣ Run CipherGist  
```sh
python ciphergist.py
```
If it’s your first time running, it will ask for:  
🔹 **GitHub Token**  
🔹 **Gist ID**  

These will be stored in `config.txt` for future use.  

---

## 🔑 How to Use  

📤 **Sending a Message:**  
1. Type your message and hit Enter.  
2. The message gets encrypted and stored in your **Gist**.  
3. Your friend with the same **config.txt** can decrypt it.  

📥 **Receiving Messages:**  
1. The program checks your Gist every **3 seconds**.  
2. If a new encrypted message is found, it **automatically decrypts and displays** it.  

⚠️ **IMPORTANT:**  
**Both you and your friend must use the same `config.txt`** for the conversation to work!  

---

## 🔐 Is CipherGist Secure?  
✔ **Uses NaCl cryptography (Ed25519 & X25519)** – trusted by security experts.  
✔ **No passwords stored** – keys are generated per session.  
✔ **No central server** – GitHub can't read your encrypted messages.  
✔ **No metadata leaks** – only encrypted text is uploaded to Gists.  
✔ **Self-hosted & auditable** – you control the encryption keys.  

---

## 📝 Future Plans  
🚀 **Mobile App** – A mobile version for Android/iOS.
🔒 **Multi-User Chat Support** – Secure group conversations.  

---

### 🎯 Start Encrypting Today!  
**Forget about centralized messengers.** Take control of your privacy with **CipherGist**.
