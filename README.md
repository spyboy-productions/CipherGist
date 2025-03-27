<h4 align="center"> If you find this GitHub repo useful, please consider giving it a star! ⭐️ </h4> 
<p align="center">
    <a href="https://spyboy.in/twitter">
      <img src="https://img.shields.io/badge/-TWITTER-black?logo=twitter&style=for-the-badge">
    </a>
    &nbsp;
    <a href="https://spyboy.in/">
      <img src="https://img.shields.io/badge/-spyboy.in-black?logo=google&style=for-the-badge">
    </a>
    &nbsp;
    <a href="https://spyboy.blog/">
      <img src="https://img.shields.io/badge/-spyboy.blog-black?logo=wordpress&style=for-the-badge">
    </a>
    &nbsp;
    <a href="https://spyboy.in/Discord">
      <img src="https://img.shields.io/badge/-Discord-black?logo=discord&style=for-the-badge">
    </a>
  
</p>

<p align="center">
  <img width="20%" src="https://github.com/spyboy-productions/CipherGist/blob/main/CipherGist.webp" />
</p>

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

## 📊 CipherGist vs Other Messengers – Feature Comparison  

| Feature                  | **CipherGist** 🛡️ | **Signal** 🔵 | **Telegram** ✈️ | **WhatsApp** ✅ | **Email (PGP)** 📧 |
|--------------------------|:-----------------:|:------------:|:--------------:|:--------------:|:---------------:|
| **End-to-End Encryption** | ✅ **Yes** (NaCl - X25519) | ✅ Yes (Signal Protocol) | ⚠️ Secret Chats Only | ✅ Yes | ✅ Yes (PGP) |
| **Requires Phone Number** | ❌ **No** | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No |
| **Server Storage** | ❌ **None** (Uses GitHub Gist) | ✅ Yes (Signal servers) | ✅ Yes (Cloud-based) | ✅ Yes (Meta servers) | ❌ No |
| **Metadata Collection** | ❌ **No** (Only encrypted text in Gist) | ⚠️ Some (Stores who you contact) | ⚠️ High (Cloud sync) | 🚨 **Very High** (Metadata & backups) | ❌ No |
| **Self-Hosted Option** | ✅ **Yes** (Your own Gist) | ❌ No | ❌ No | ❌ No | ✅ Yes (Own mail server) |
| **Message Deletion** | ✅ **Fully Controllable** (Delete Gist) | ✅ Yes (Disappearing messages) | ✅ Yes | ✅ Yes | ✅ Yes |
| **Group Chat Support** | ❌ Not yet | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No |
| **Multi-Device Support** | ✅ Yes (Cross-platform) | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **Third-Party Tracking** | ❌ **None** | ❌ No | ✅ Yes (Cloud storage) | ✅ Yes (Meta tracking) | ❌ No |
| **Dependencies** | 🔹 Python, GitHub Gist | 🔹 Signal App | 🔹 Telegram App | 🔹 WhatsApp App | 🔹 PGP Tools |
| **Message Delivery** | 🔄 **Polls Gist every 3 sec** | 📩 Push Notifications | 📩 Push Notifications | 📩 Push Notifications | 📩 Email |
| **Open-Source** | ✅ **Yes** | ✅ Yes | ⚠️ Partially | ❌ No | ✅ Yes |
| **Data Ownership** | ✅ **You own your messages** | ❌ No | ❌ No | ❌ No | ✅ Yes |
| **Best Use Case** | 🔐 **Anonymous Secure Chat** | 🔵 Private Messaging | 🔹 Casual & Cloud Backup | ✅ Friends & Family | 📧 Email Security |

🚀 **Conclusion:**  
CipherGist is the **most private and self-hosted** option, ideal for those who want **no central servers, no phone numbers, and full control over encryption keys.** However, it's not as user-friendly as mainstream messengers and currently lacks group chat features.

---

## 🛠️ Installation & Setup  

### 1️⃣ Installation
```bash
git clone https://github.com/spyboy-productions/CipherGist.git
```
```
cd CipherGist
```
```
pip install -r requirements.txt
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
python CipherGistt.py
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
