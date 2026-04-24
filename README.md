# Albania Blood Cybersecurity — iOS Security Analyzer

![Security](https://img.shields.io/badge/security-high-green)
![License](https://img.shields.io/badge/license-MIT-blue)

## About

`iOS Security Analyzer` is a Python-based security auditing utility intended for iOS-oriented environments (including iSH-like setups) and other Unix-like systems where required tools are available.

It provides:

- System information collection.
- Running process inspection.
- Wi-Fi scan attempts (via `nmcli` when available).
- Security report generation to a local output folder.

## Installation

### 1) Clone the repository

```bash
git clone https://github.com/youh4ck3dme/ios-security-analyzer.git
cd ios-security-analyzer
```

### 2) Create and activate a virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install --upgrade pip
pip install psutil
```

## Dependencies

The project currently requires:

- Python 3.8+
- [`psutil`](https://pypi.org/project/psutil/)

Optional/runtime environment dependencies:

- `nmcli` (NetworkManager CLI), required only for Wi-Fi scanning.
- A shell environment that supports ANSI output formatting (for colorized terminal output).

## Usage

Run the tool:

```bash
python3 ios_security_analyzer.py
```

Menu options:

1. Scan System Info
2. List Running Processes
3. Scan Wi-Fi Networks
4. Generate Security Report
5. Exit

### Non-interactive quick checks (optional)

```bash
python3 -m py_compile ios_security_analyzer.py
```

## Output / Report Location

When you choose **Generate Security Report**, the tool creates:

- `output/system_report.txt`

Path details:

- The `output/` directory is auto-created if missing.
- Existing report files are overwritten by default.

## Troubleshooting

### `ModuleNotFoundError: No module named 'psutil'`

Install dependency in your current environment:

```bash
pip install psutil
```

### Wi-Fi scan says unavailable

This is expected when:

- `nmcli` is not installed.
- The environment is sandboxed (common on mobile/iOS containers).
- Required system permissions are not available.

The script falls back to a message and continues execution.

### `socket.gaierror` or invalid host/IP behavior

Hostname resolution may fail in restricted network environments. Re-run in a network-enabled shell or verify local resolver configuration.

### Permission errors writing report

Ensure the current user can write to the repository directory:

```bash
mkdir -p output && touch output/system_report.txt
```

### ANSI color output appears garbled

Use a terminal emulator with ANSI color support, or remove escape sequences from the script if needed for plain-text environments.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
