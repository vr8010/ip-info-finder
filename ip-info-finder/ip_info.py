#!/usr/bin/env python3
"""
IP Info Finder - A CLI tool for IP geolocation lookup
"""

import requests
import json
import sys


def validate_ip(ip_address):
    """Basic IP address validation"""
    parts = ip_address.split('.')
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False


def get_ip_info(ip_address):
    """Fetch IP information from ip-api.com"""
    api_url = f"http://ip-api.com/json/{ip_address}"
    
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get('status') == 'fail':
            return None, data.get('message', 'Unknown error')
        
        return data, None
    
    except requests.exceptions.ConnectionError:
        return None, "Network connection error. Please check your internet connection."
    except requests.exceptions.Timeout:
        return None, "Request timed out. Please try again."
    except requests.exceptions.RequestException as e:
        return None, f"API request failed: {str(e)}"
    except json.JSONDecodeError:
        return None, "Failed to parse API response."


def display_ip_info(data):
    """Display IP information in a formatted manner"""
    print("\n" + "="*40)
    print("IP Address : " + data.get('query', 'N/A'))
    print("Country    : " + data.get('country', 'N/A'))
    print("Region     : " + data.get('regionName', 'N/A'))
    print("City       : " + data.get('city', 'N/A'))
    print("ZIP Code   : " + data.get('zip', 'N/A'))
    print("Latitude   : " + str(data.get('lat', 'N/A')))
    print("Longitude  : " + str(data.get('lon', 'N/A')))
    print("ISP        : " + data.get('isp', 'N/A'))
    print("Organization : " + data.get('org', 'N/A'))
    print("Timezone   : " + data.get('timezone', 'N/A'))
    print("="*40 + "\n")


def main():
    """Main function to run the IP Info Finder"""
    print("\n=== IP Info Finder ===\n")
    
    # Get IP address from user
    ip_address = input("Enter IP Address: ").strip()
    
    # Validate IP address
    if not validate_ip(ip_address):
        print("\n❌ Error: Invalid IP address format.")
        print("Please enter a valid IPv4 address (e.g., 8.8.8.8)")
        sys.exit(1)
    
    # Fetch IP information
    print("\n🔍 Fetching information...")
    data, error = get_ip_info(ip_address)
    
    if error:
        print(f"\n❌ Error: {error}")
        sys.exit(1)
    
    # Display results
    display_ip_info(data)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user.")
        sys.exit(0)
