# 🌐 IP Info Finder

A command-line tool for retrieving geolocation and network information about IP addresses using public APIs.

## 📋 Description

IP Info Finder is a Python-based CLI tool that helps users learn about basic network reconnaissance and cybersecurity concepts. It queries public IP geolocation APIs to retrieve detailed information about any IPv4 address.

## ✨ Features

- 🔍 IP geolocation lookup
- 🌍 Country, region, and city information
- 📍 Latitude and longitude coordinates
- 🏢 ISP and organization detection
- 🕐 Timezone information
- ⚡ Simple CLI interface
- 🛡️ Comprehensive error handling
- ✅ IP address validation

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/ip-info-finder.git
cd ip-info-finder
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

Run the tool:
```bash
python ip_info.py
```

Follow the prompt to enter an IP address.

## 📖 Example Output

```
=== IP Info Finder ===

Enter IP Address: 8.8.8.8

🔍 Fetching information...

========================================
IP Address : 8.8.8.8
Country    : United States
Region     : California
City       : Mountain View
ZIP Code   : 94035
Latitude   : 37.386
Longitude  : -122.0838
ISP        : Google LLC
Organization : Google Public DNS
Timezone   : America/Los_Angeles
========================================
```

## 📊 IP Information Fields Explained

- **IP Address**: The queried IPv4 address
- **Country**: The country where the IP is registered
- **Region**: State or province
- **City**: City location
- **ZIP Code**: Postal code of the location
- **Latitude/Longitude**: Geographic coordinates
- **ISP**: Internet Service Provider
- **Organization**: Company or entity that owns the IP
- **Timezone**: Local timezone of the IP location

## 🛠️ Requirements

- Python 3.6+
- requests library

## ⚠️ Error Handling

The tool handles:
- Invalid IP address formats
- Network connection issues
- API errors and timeouts
- Keyboard interrupts

## 📡 API Information

This tool uses the free [ip-api.com](http://ip-api.com) service. Please note:
- Free for non-commercial use
- Rate limit: 45 requests per minute
- No API key required

## 👤 Author

Your Name

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ⚡ Quick Tips

- Try public DNS servers: `8.8.8.8` (Google), `1.1.1.1` (Cloudflare)
- Use your own public IP to see your location
- Educational tool - use responsibly and ethically
