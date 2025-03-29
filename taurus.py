import os
import requests
from termcolor import colored

def scan_url(url):
    print(colored(f"Scanning URL: {url}", "cyan"))
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(colored("[SUCCESS] URL is accessible.", "green"))
        else:
            print(colored(f"[WARNING] URL returned status code {response.status_code}.", "yellow"))
    except requests.exceptions.RequestException as e:
        print(colored(f"[ERROR] Failed to access URL: {e}", "red"))

def scan_ports(ip):
    print(colored(f"Scanning ports on IP: {ip}", "cyan"))
    common_ports = [21, 22, 80, 443, 3306]
    for port in common_ports:
        result = os.system(f"nc -zv {ip} {port} > /dev/null 2>&1")
        if result == 0:
            print(colored(f"[OPEN] Port {port} is open.", "green"))
        else:
            print(colored(f"[CLOSED] Port {port} is closed.", "red"))

def main():
    print(colored("Automated Vulnerability Scanner", "blue", attrs=["bold"]))
    choice = input("Enter '1' to scan a URL or '2' to scan an IP for open ports: ")
    
    if choice == '1':
        url = input("Enter the URL to scan: ")
        scan_url(url)
    elif choice == '2':
        ip = input("Enter the IP address to scan: ")
        scan_ports(ip)
    else:
        print(colored("[ERROR] Invalid choice.", "red"))

if __name__ == "__main__":
    main()
