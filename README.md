# 🔎 ShowMetheIP 🔍  
**Internet Protocol Show Information**  
🐍 *Python-based tool* 🐍  
🔎 *IP Show Information Utility* 🔎  

## 📌 Description  
A console-based tool to display detailed information about any public IP address using the [ip-api.com](http://ip-api.com/) API. Perfect for learning about IP geolocation or for OSINT investigations.  

## 💻 Features  
- IP address validation  
- HTTP requests to `ip-api.com`  
- Clean styled output using Colorama and Pystyle  
- Optional logging to `ip_log.txt`  
- Terminal-like interface with username display  

## 📼 Installation  
Install Python, Git, and clone the repo, then install requirements. The commands vary slightly depending on your environment.

For **Linux (Debian/Ubuntu)** and **Termux (Android)**, run these commands:

```bash
# Install Python and Git
# Linux:
apt install python3 git
# Termux:
pkg install python3 git

# Clone the repo
git clone https://github.com/know56All1/showmetheip
cd showmetheip

# Install Python dependencies
pip install -r requirements.txt
# In Termux, if pip points to Python 2, use:
pip3 install -r requirements.txt

