# 🔴 Albania Blood Cybersecurity - iOS Security Analyzer 🔴
### Your iOS Security Guardian - Advanced Forensic & Threat Analysis for iOS

![Security](https://img.shields.io/badge/security-high-green) ![License](https://img.shields.io/badge/license-MIT-blue)

## 📌 About
**iOS Security Analyzer** is a penetration testing and security auditing utility intended for constrained/mobile Linux environments (for example iSH-style workflows on iOS).

It can:
- collect basic host/system metadata,
- inspect active processes,
- attempt Wi-Fi scan collection (when the platform supports it),
- export a text security report.

## 🚀 Features
- ✅ Automated security auditing
- ✅ System information analysis
- ✅ Process monitoring (CPU & RAM usage)
- ✅ Wi-Fi network scanning (platform/privilege dependent)
- ✅ Security report generation (`output/system_report.txt`)

## 📋 Requirements
- Python **3.9+**
- Python package: `psutil`
- Optional system tool for Wi-Fi scan: `nmcli`

> Notes:
> - In many iOS sandboxed environments, Wi-Fi scan is unavailable.
> - If `nmcli` is not installed (or Wi-Fi access is blocked), the tool records a graceful fallback message in output/report.

## 📥 Installation
```sh
git clone https://github.com/youh4ck3dme/ios-security-analyzer.git
cd ios-security-analyzer
python3 -m pip install --upgrade pip
python3 -m pip install psutil
```

## ▶️ Usage
Run interactively:
```sh
python3 ios_security_analyzer.py
```

Menu options:
1. Scan System Info
2. List Running Processes
3. Scan Wi-Fi Networks
4. Generate Security Report
5. Exit

## 📁 Report Output
When you choose **Generate Security Report**, a report is saved to:
```txt
output/system_report.txt
```

The report includes:
- system information,
- top running processes,
- Wi-Fi scan output or fallback status.

## 🧪 Quick Validation
```sh
python3 -m py_compile ios_security_analyzer.py
python3 ios_security_analyzer.py
```

## ⚠️ Troubleshooting
- `ModuleNotFoundError: psutil`:
  - install with `python3 -m pip install psutil`
- Wi-Fi scan unavailable:
  - expected on restricted environments; this is handled gracefully.
- Host/IP resolution failure:
  - analyzer now falls back to `unavailable` values and continues.

## 📜 License
MIT License (see `LICENSE`).
