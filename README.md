# 🔴 Albania Blood Cybersecurity - iOS Security Analyzer
### **Your iOS Security Guardian - Advanced Forensic & Threat Analysis for iOS**
### **Advanced iOS Cybersecurity & Pentesting Tool**

![Security](https://img.shields.io/badge/security-high-green) ![License](https://img.shields.io/badge/license-MIT-blue)

## 📌 About
**iOS Security Analyzer** is a penetration testing and security auditing tool designed for **iSH on iOS**. It can collect system information, inspect running processes, attempt Wi-Fi scanning, and export a basic security report.

## 🚀 Features
- ✅ Automated security auditing
- ✅ System information analysis
- ✅ Process monitoring (CPU & RAM usage)
- ✅ Wi-Fi network scanning (when available)
- ✅ Security report generation (export logs)

## ✅ Requirements
- **Python:** Python **3.8+** is recommended.
- **Python package:** `psutil` must be installed.
- **Wi-Fi scanner dependency:** Wi-Fi scanning uses `nmcli` (`nmcli dev wifi`).
  - On most **iOS/iSH** environments, `nmcli` is missing or blocked by sandbox limitations.
  - If `nmcli` is unavailable, the tool will show:
    - `Wi-Fi scan unavailable on iOS sandbox.`

### Interpreting Wi-Fi scan output
- If actual network rows are shown, scanning worked in your environment.
- If you only see `Wi-Fi scan unavailable on iOS sandbox.`, this is expected on restricted iOS setups and **does not mean the script crashed**.
- Report generation still works; only the Wi-Fi section is limited.

## ⚡ Quickstart
```sh
# 1) (Optional) create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2) Install dependencies
python3 -m pip install --upgrade pip
python3 -m pip install psutil

# 3) Run the analyzer
python3 ios_security_analyzer.py
```

## 📥 Installation (Git)
```sh
git clone https://github.com/youh4ck3dme/ios-security-analyzer.git
cd ios-security-analyzer
python3 -m pip install psutil
python3 ios_security_analyzer.py
```
