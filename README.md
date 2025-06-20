# 🧩 File Integrity Checker

A lightweight Python tool to monitor critical system or configuration files for unauthorized changes using SHA-256 hash verification.

## 🔐 Features
- Monitors selected files for tampering
- Alerts on any unauthorized modification
- Logs every change with timestamp

## 📦 Tech Stack
- Python 3.x
- hashlib

## ⚙️ How to Use
1. List sensitive files in `FILES_TO_MONITOR`.
2. Run the tool:
```bash
python3 file_integrity_checker.py
Monitor for alerts in console or file_alerts.log.
