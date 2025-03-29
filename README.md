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

Move the script to /usr/local/bin for global access:

sudo mv vulnerability_scanner.py /usr/local/bin/vulnerability_scanner
chmod +x /usr/local/bin/vulnerability_scanner
