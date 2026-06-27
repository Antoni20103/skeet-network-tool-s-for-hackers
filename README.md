# SKEET - Professional Network Security Toolkit

![SKEET Logo](https://img.shields.io/badge/SKEET-Network%20Toolkit-blue)
![Python](https://img.shields.io/badge/Python-3.8+-brightgreen)
![Status](https://img.shields.io/badge/Status-Active-success)

**SKEET** is a comprehensive network penetration testing and security analysis toolkit built with Python. It combines 11 powerful networking tools into one elegant, user-friendly interface.

## 🎯 Features

### Core Tools
- **Scanner** - Advanced port scanning with SYN reconnaissance
- **Sniffer** - Network packet capture and analysis
- **DoS Attack** - Single-threaded denial of service attacks
- **DDoS Attack** - Multi-threaded distributed denial of service
- **Deauth Attack** - WiFi deauthentication for device disconnection
- **Network Mapping** - Network topology discovery and visualization
- **ARP Spoofing** - Man-in-the-Middle attack capabilities
- **Bluetooth Scanner** - Bluetooth device detection and enumeration
- **Fake WiFi** - Rogue access point simulation (macOS compatible)

### User Experience
- 🌈 Beautiful gradient ASCII art logo
- 🎨 Rich color-coded interface (bright_blue, cyan, green, red)
- 📱 Device OS identification (iPhone, Android, macOS, etc.)
- 🔐 MAC address vendor recognition
- ⚡ Real-time device monitoring
- 💻 Interactive menu-driven interface

## 📋 Requirements

### System Requirements
- **OS**: Linux (Kali preferred), macOS, or Windows (WSL)
- **Python**: 3.8 or higher
- **Permissions**: Root/sudo access for most features

### Python Dependencies
```
nmap==0.0.1
scapy==2.5.0
rich==13.0.0
colorama==0.4.6
```

### Optional Hardware
- **WiFi Card**: TP-Link TL-WN722N or Alfa AWUS036H (for advanced WiFi attacks)
- For monitor mode: Card supporting monitor mode and packet injection

## 🚀 Installation

### Step 1: Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/skeet.git
cd skeet
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Install System Tools
```bash
# On Kali Linux / Debian
sudo apt-get install nmap hostapd dnsmasq

# On macOS
brew install nmap hostapd dnsmasq
```

## 💻 Usage

### Basic Launch
```bash
sudo python3 skeet.py
```

### Interactive Menu
```
███████╗██╗  ██╗███████╗███████╗████████╗
██╔════╝██║ ██╔╝██╔════╝██╔════╝╚══██╔══╝
███████╗█████╔╝ █████╗  █████╗     ██║
╚════██║██╔═██╗ ██╔══╝  ██╔══╝     ██║
███████║██║  ██╗███████╗███████╗   ██║
╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝

welcome in skeet!
skeet is network tools for hackers

MENU:
1. Scanner
2. Sniffer
3. DoS Attack
4. DDoS Attack
5. Deauth Attack
6. Network Mapping
7. ARP Spoofing
8. Bluetooth Scanner
9. Fake WiFi
10. Help
11. Exit

Enter choice: _
```

## 📚 Tool Documentation

### 1. Scanner
Scans target IP for open ports using SYN scan technique.
```bash
Enter choice: 1
Enter the target IP: 192.168.1.1
```

### 2. Sniffer
Captures network packets from specific IP addresses.
```bash
Enter choice: 2
Enter the target IP: 192.168.1.100
```

### 3. DoS Attack
Single-threaded UDP packet flood attack.
```bash
Enter choice: 3
Enter the target IP: target.com
Enter the target port: 80
Enter the number of packets: 1000
```

### 4. DDoS Attack
Multi-threaded distributed denial of service.
```bash
Enter choice: 4
Enter the target IP: target.com
Enter the target port: 80
Enter number of threads: 10
Enter duration in seconds: 30
```

### 5. Deauth Attack
Sends deauthentication frames to disconnect devices from WiFi.
```bash
Enter choice: 5
Enter target MAC address: 00:1A:2B:3C:4D:5E
Enter interface: en0
Enter number of deauth packets: 100
```

### 6. Network Mapping
Scans network range and displays connected devices.
```bash
Enter choice: 6
```
Automatically scans 192.168.1.0/24 subnet.

### 7. ARP Spoofing
Performs ARP spoofing for Man-in-the-Middle attacks.
```bash
Enter choice: 7
Enter gateway IP: 192.168.1.1
Enter target IP: 192.168.1.100
Enter interface: en0
```

### 8. Bluetooth Scanner
Scans for nearby Bluetooth devices.
```bash
Enter choice: 8
```

### 9. Fake WiFi
Creates rogue WiFi hotspot (macOS/Linux).
```bash
Enter choice: 9
Enter SSID: FreeWiFi
Add password: y/n
```

## ⚙️ Configuration

### Network Interface Selection
For WiFi attacks, select appropriate interface:
- **macOS**: `en0` (usually WiFi), `en1` (secondary)
- **Linux**: `wlan0`, `wlan1` (WiFi), `eth0` (Ethernet)

### Target IP Ranges
- Local network: `192.168.1.0/24`
- Custom range: Adjust in Network Mapping tool

## 🛡️ Security & Ethics

**⚠️ IMPORTANT DISCLAIMER**

This toolkit is for **authorized security testing only**:
- ✅ Test on networks you own or have written permission
- ✅ Educational purposes and penetration testing
- ❌ Illegal unauthorized access
- ❌ Attacks on systems without permission

**Legal Consequences**:
- Unauthorized network attacks violate CFAA (Computer Fraud and Abuse Act)
- Potential jail time and fines
- Civil liability for damages

**Responsible Use**:
- Always get written permission before testing
- Use in controlled environments
- Report vulnerabilities responsibly
- Follow ethical hacking guidelines (EC-Council, CompTIA Security+)

## 🔧 Advanced Features

### MAC Address Identification
Automatically identifies device types based on MAC address:
- Apple (iOS/macOS)
- Samsung (Android)
- Google devices
- Microsoft products

### OS Detection
Identifies operating systems of connected devices:
- iOS/macOS
- Android
- Windows
- Linux

### Real-time Monitoring
Live monitoring of network connections and device status.

## 📊 System Requirements by Tool

| Tool | Requirements | Difficulty |
|------|--------------|-----------|
| Scanner | nmap | Easy |
| Sniffer | Root/sudo | Medium |
| DoS | Root/sudo | Easy |
| DDoS | Root/sudo | Easy |
| Deauth | Monitor mode WiFi | Hard |
| Network Map | nmap | Easy |
| ARP Spoofing | Root/sudo | Hard |
| Bluetooth | Bluetooth adapter | Medium |
| Fake WiFi | Secondary WiFi card | Very Hard |

## 🐛 Troubleshooting

### "Permission denied" errors
```bash
sudo python3 skeet.py
```

### nmap not found
```bash
sudo apt-get install nmap  # Linux
brew install nmap          # macOS
```

### No WiFi interface available
Check available interfaces:
```bash
ifconfig      # macOS/Linux
ipconfig      # Windows
```

### Deauth not working
Requires monitor mode support:
```bash
sudo airmon-ng start wlan0
```

## 📈 Future Updates

Planned features:
- [ ] SSL Strip implementation
- [ ] DNS Spoofing
- [ ] Packet injection
- [ ] Web vulnerability scanner
- [ ] Social engineering tools
- [ ] Credential harvesting
- [ ] Multi-target support
- [ ] Logging to database

## 📖 Learning Resources

### Recommended Reading
- "Black Hat Python" by Justin Seitz
- "The Art of Network Penetration Testing" by Royce Davis
- "Network Security Assessment" by Chris McNab

### Online Courses
- OSCP (Offensive Security Certified Professional)
- CEH (Certified Ethical Hacker)
- CompTIA Security+

### Practice Platforms
- HackTheBox
- TryHackMe
- OWASP WebGoat

## 🤝 Contributing

Contributions welcome! Areas of interest:
- Bug fixes
- Performance improvements
- New tools/features
- Documentation
- Test cases

## 👨‍💻 Author

**Antoni** - Security Researcher & Developer
- Penetration tester

## 📝 License

License will be added soon. All rights reserved for now.

**Copyright © 2026 SKEET Project**

---

## ⚡ Quick Start

```bash
# Clone
git clone https://github.com/YOUR_USERNAME/skeet.git

# Install
cd skeet
pip install -r requirements.txt

# Run
sudo python3 skeet.py

# Select tool from menu
Enter choice: 1
```

## 🎓 Educational Disclaimer

This project is designed for:
- ✅ Learning network security
- ✅ Understanding attack vectors
- ✅ Authorized penetration testing
- ✅ Security research
- ❌ Illegal activities

---

**Stay ethical. Stay legal. Stay awesome.** 🚀

**Last Updated**: March 29, 2026
**Version**: 1.0
**Status**: Active Development
