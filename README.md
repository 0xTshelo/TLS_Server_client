# Secure Network Communication Projects (School Assignment)
This repository contains a collection of Python-based network communication systems developed as part of a **school assignment**. Each project simulates a real-world networking scenario, focusing on **security**, **performance**, and **reliability** using protocols like **TLS**, **DNS**, **TCP**, and **UDP**.

## 📁 Project 1: Secure File Transfer with TLS

**Scenario:** A financial company needs to exchange confidential reports between branches using a secure channel.

### Implementations:

- ✅ `question 1.1.py` — Listens for secure file transfer requests.
- ✅ `question 1.2.py` — Sends files securely over TLS.
- ✅ `question 1.3py` — Enhanced server requiring client certificate authentication.
- 📄 `question 1.4.py` — Explains why TLS is critical for secure file transfers.


---

## 🌐 Project 2: DNS Optimization and Security

**Scenario:** A video streaming platform aims to reduce latency and prevent DNS-based attacks.

### Implementations:

- ✅ `question 2.1.py` — Queries multiple DNS servers in parallel and selects the fastest.
- ✅ `question 2.2.py` — Implements DNSSEC to prevent cache poisoning.
- ✅ `question 2.3.py` — Distributes DNS queries based on load.
- ✅ `question 2.4.py` — Performs DNS-over-HTTPS (DoH) using Python's `requests`.
- ✅ `question 2.5.py` — Custom DNS cache with expiration.

---

## 📦 Project 3: Reliable File Transfer with TCP

**Scenario:** A system to upload/download files between client and server using reliable TCP communication.

### Implementations:

- ✅ `question 3.1.py` — Handles multiple clients via multithreading; receives and sends files.
- ✅ `question 3.2.py` — Uploads files to and downloads files from the server.

---

## 💬 Project 4: UDP-Based Chat System

**Scenario:** A simple chat application allowing clients to broadcast and receive messages using UDP.

### Implementations:

- ✅ `question 4.1.py` — Listens for messages and broadcasts them to all connected clients.
- ✅ `question 4.2.py` — Sends messages to the server and displays received ones.

---

## 📎 Note

All files in this repository were developed as part of a **school assignment** focused on network programming and security principles. Each directory includes complete, well-commented Python source code.

---

## 🛠️ Requirements

- Python 3.7+
- `requests` (for DNS-over-HTTPS)
- OpenSSL (for TLS mutual authentication)
