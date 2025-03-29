# Tools-Taurus

Features
URL Scanning: Checks if a URL is accessible and returns HTTP status codes.

Port Scanning: Scans common ports (e.g., 21, 22, 80, etc.) on a given IP address.

Colored Output: Uses termcolor for better visibility of results.

Step 2: Installation Tutorial
Prerequisites
Python 3 installed on Linux.

Install required libraries (requests, termcolor):
pip install requests termcolor
Installation Steps
Save the code above in a file named vulnerability_scanner.py.

Below is a step-by-step guide to creating an automated vulnerability scanner tool using Python. The tool will feature colored output for better readability and will be designed for Linux installation.

---

### Features
- **URL Scanning**: Checks if a URL is accessible and returns HTTP status codes.
- **Port Scanning**: Scans common ports (e.g., 21, 22, 80, etc.) on a given IP address.
- **Colored Output**: Uses `termcolor` for better visibility of results.

---

## **Step 2: Installation Tutorial**

### Prerequisites
1. Python 3 installed on Linux.
2. Install required libraries (`requests`, `termcolor`):
   ```bash
   pip install requests termcolor
   ```

### Installation Steps
1. Save the code above in a file named `vulnerability_scanner.py`.
2. Move the script to `/usr/local/bin` for global access:
   ```bash
   sudo mv taurus.py /usr/local/bin/vulnerability_scanner
   chmod +x /usr/local/bin/taurus.py
   ```

---

## **Step 3: Usage Tutorial**

### Running the Tool
1. Open your terminal.
2. Run the tool using:
   ```bash
  taurus.py
   ```
3. Follow the prompts to either scan a URL or an IP address.

### Example Commands
- Scan a URL:
  ```bash
  Enter '1' to scan a URL or '2' to scan an IP for open ports: 1
  Enter the URL to scan: https://example.com
  ```
- Scan an IP for open ports:
  ```bash
  Enter '1' to scan a URL or '2' to scan an IP for open ports: 2
  Enter the IP address to scan: 192.168.1.1
  ```


This tool provides basic vulnerability scanning functionality with enhanced readability using colors. You can expand it further by integrating more advanced features, such as CVE detection or database scanning.
