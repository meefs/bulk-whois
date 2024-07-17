import whois
from ipwhois import IPWhois
import socket
import concurrent.futures
import sys
import ipaddress

def is_ip_address(host):
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False

def get_whois_info(host):
    try:
        if is_ip_address(host):
            ip = host
        else:
            ip = socket.gethostbyname(host)
        
        # Get IP whois information
        ip_info = IPWhois(ip).lookup_rdap()
        
        # Extract AS number and name
        asn = ip_info.get('asn')
        as_name = ip_info.get('asn_description')
        
        # Get country
        country = ip_info.get('asn_country_code')
        
        return {
            'host': host,
            'ip': ip,
            'asn': asn,
            'as_name': as_name,
            'country': country
        }
    except Exception as e:
        return {
            'host': host,
            'error': str(e)
        }

def bulk_whois_lookup(hosts):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(get_whois_info, hosts))
    return results

def print_usage():
    print("Usage:")
    print("  1. Pipe a list of hostnames or IP addresses:")
    print("     cat hosts.txt | python script.py")
    print("  2. Enter hostnames or IP addresses interactively:")
    print("     python script.py")
    print("     Then enter hostnames or IPs, one per line. Press Ctrl+D (Unix) or Ctrl+Z (Windows) to finish.")
    print("  3. Provide hostnames or IP addresses as command-line arguments:")
    print("     python script.py google.com 8.8.8.8")

def main():
    if sys.stdin.isatty():
        # No input piped, check if there are command-line arguments
        if len(sys.argv) > 1:
            hosts = sys.argv[1:]
        else:
            print_usage()
            print("\nEnter hostnames or IP addresses (one per line), then press Ctrl+D (Unix) or Ctrl+Z (Windows) when finished:")
            hosts = [line.strip() for line in sys.stdin]
    else:
        # Input is piped
        hosts = [line.strip() for line in sys.stdin]

    if not hosts:
        print("No hosts or IP addresses provided. Exiting.")
        sys.exit(1)

    print("Starting bulk Whois lookup...")
    results = bulk_whois_lookup(hosts)
    
    for result in results:
        if 'error' in result:
            print(f"Error for {result['host']}: {result['error']}")
        else:
            print(f"Host/IP: {result['host']}")
            print(f"IP: {result['ip']}")
            print(f"ASN: {result['asn']}")
            print(f"AS Name: {result['as_name']}")
            print(f"Country: {result['country']}")
            print("-" * 40)

if __name__ == "__main__":
    main()
