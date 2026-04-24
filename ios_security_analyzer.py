#!/usr/bin/env python3
import os
import platform
import psutil
import socket
import time
import subprocess

def format_probe_error(probe_name, error):
    """Return a normalized error string for probe failures."""
    return f"unavailable ({probe_name}: {error.__class__.__name__}: {error})"

# 🔴 Albania Blood Cybersecurity Banner
def print_banner():
    banner = """
    \033[1;31m  █████╗ ██╗     ██████╗  █████╗ ███╗   ██╗██╗ █████╗    
    ██╔══██╗██║     ██╔══██╗██╔══██╗████╗  ██║██║██╔══██╗   
    ███████║██║     ██████╔╝███████║██╔██╗ ██║██║███████║   
    ██╔══██║██║     ██╔═══╝ ██╔══██║██║╚██╗██║██║██╔══██║   
    ██║  ██║███████╗██║     ██║  ██║██║ ╚████║██║██║  ██║   
    ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝   
   
    \033[1;37m██████╗ ██╗      ██████╗  ██████╗ ███████╗███████╗
    ██╔══██╗██║     ██╔═══██╗██╔═══██╗██╔════╝██╔════╝
    ██████╔╝██║     ██║   ██║██║   ██║███████╗███████╗
    ██╔═══╝ ██║     ██║   ██║██║   ██║╚════██║╚════██║
    ██║     ███████╗╚██████╔╝╚██████╔╝███████║███████║
    ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
    
    \033[1;35m👾🪬 CYBERSECURITY AUDIT TOOL 🪬👾
    """
    print(banner)

# 🔎 Get System Information
def get_system_info():
    hostname = "unavailable"
    ip_address = "unavailable"

    try:
        hostname = socket.gethostname()
    except OSError as e:
        hostname = format_probe_error("hostname resolution", e)

    if hostname == "unavailable":
        ip_address = "unavailable"
    else:
        try:
            ip_address = socket.gethostbyname(hostname)
        except socket.gaierror as e:
            ip_address = format_probe_error("ip resolution", e)

    system_info = {
        "OS": platform.system(),
        "Version": platform.version(),
        "Release": platform.release(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Hostname": hostname,
        "IP Address": ip_address,
        "Uptime": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(psutil.boot_time()))
    }
    return system_info

# 🖥️ Get Running Processes
def get_running_processes():
    processes = []
    try:
        process_iter = psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])
    except (psutil.Error, OSError) as e:
        return [{
            "pid": "unavailable",
            "name": format_probe_error("process iteration", e),
            "cpu_percent": "unavailable",
            "memory_percent": "unavailable"
        }]

    for proc in process_iter:
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, OSError) as e:
            processes.append({
                "pid": "unavailable",
                "name": format_probe_error("process read", e),
                "cpu_percent": "unavailable",
                "memory_percent": "unavailable"
            })
    return processes

# 📡 Wi-Fi Network Scan (Requires Jailbreak/Root)
def get_wifi_networks():
    wifi_info = []
    try:
        result = subprocess.check_output("nmcli dev wifi", shell=True, text=True)
        wifi_info = result.split("\n")[1:]  # Ignore the first line
    except Exception as e:
        wifi_info.append("Wi-Fi scan unavailable on iOS sandbox.")
    return wifi_info

# 📂 Save Report
def save_report(system_info, processes, wifi_networks):
    report_path = "output/system_report.txt"
    os.makedirs(os.path.dirname(report_path), exist_ok=True)

    with open(report_path, "w") as f:
        f.write("### System Information ###\n")
        for key, value in system_info.items():
            f.write(f"{key}: {value}\n")
        f.write("\n### Running Processes ###\n")
        for proc in processes[:10]:  # Show only first 10 processes
            f.write(f"PID: {proc['pid']}, Name: {proc['name']}, CPU: {proc['cpu_percent']}%, Memory: {proc['memory_percent']}%\n")
        f.write("\n### Wi-Fi Networks ###\n")
        for net in wifi_networks:
            f.write(f"{net}\n")
    
    print(f"\033[1;32mReport saved to {report_path}\033[0m")  # Green color

# 🎛️ Admin Panel
def main():
    while True:
        print_banner()
        print("\033[1;33m1. Scan System Info\033[0m")  # Yellow
        print("\033[1;33m2. List Running Processes\033[0m")
        print("\033[1;33m3. Scan Wi-Fi Networks\033[0m")
        print("\033[1;33m4. Generate Security Report\033[0m")
        print("\033[1;33m5. Exit\033[0m")

        choice = input("\n\033[1;36mSelect an option: \033[0m")  # Cyan
        if choice == "1":
            info = get_system_info()
            for key, value in info.items():
                print(f"\033[1;35m{key}:\033[0m {value}")  # Purple
        elif choice == "2":
            processes = get_running_processes()
            for proc in processes[:10]:  # Show only first 10 processes
                print(f"\033[1;35mPID:\033[0m {proc['pid']}, \033[1;35mName:\033[0m {proc['name']}, \033[1;35mCPU:\033[0m {proc['cpu_percent']}%, \033[1;35mMemory:\033[0m {proc['memory_percent']}%")
        elif choice == "3":
            wifi_networks = get_wifi_networks()
            for net in wifi_networks:
                print(f"\033[1;35m{net}\033[0m")
        elif choice == "4":
            info = get_system_info()
            processes = get_running_processes()
            wifi_networks = get_wifi_networks()
            save_report(info, processes, wifi_networks)
        elif choice == "5":
            print("\033[1;31mExiting...\033[0m")  # Red
            exit()
        else:
            print("\033[1;31mInvalid choice. Try again.\033[0m")

if __name__ == "__main__":
    main()
