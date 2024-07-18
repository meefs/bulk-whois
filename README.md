# Bulk Whois Lookup Script

This Python script performs bulk Whois lookups for both hostnames and IP addresses, providing information such as IP address, ASN (Autonomous System Number), AS Name, associated country, and CIDR range. It supports CSV output for easy data processing and analysis.

## Features

- Supports both hostnames and IP addresses
- Performs bulk lookups concurrently for improved efficiency
- Accepts input via stdin, command-line arguments, or interactive input
- Provides detailed error messages for failed lookups
- Includes CIDR range information for each IP address
- Offers CSV output option for easy data processing

## Prerequisites

Before running the script, make sure you have Python 3.6 or higher installed. You'll also need to install the following Python modules:

```
pip install ipwhois python-whois
```

## Usage

The script is named `bulk-whois-lookup.py`. You can use it in one of the following ways:

1. Pipe a list of hostnames or IP addresses:
   ```
   cat hosts.txt | python bulk-whois-lookup.py [--csv output.csv]
   ```

2. Enter hostnames or IP addresses interactively:
   ```
   python bulk-whois-lookup.py [--csv output.csv]
   ```
   Then enter hostnames or IPs, one per line. Press Ctrl+D (Unix) or Ctrl+Z (Windows) to finish.

3. Provide hostnames or IP addresses as command-line arguments:
   ```
   python bulk-whois-lookup.py google.com 8.8.8.8 facebook.com 1.1.1.1 [--csv output.csv]
   ```

To output the results to a CSV file, add the `--csv` flag followed by the desired output filename:

```
python bulk-whois-lookup.py google.com 8.8.8.8 --csv results.csv
```

## Examples

### Example 1: Using a mix of hostnames and IP addresses with console output

```
$ python bulk-whois-lookup.py google.com 8.8.8.8 facebook.com 1.1.1.1

Starting bulk Whois lookup...
Host/IP: google.com
IP: 142.250.180.78
ASN: 15169
AS Name: GOOGLE
Country: US
CIDR: 142.250.0.0/15
----------------------------------------
Host/IP: 8.8.8.8
IP: 8.8.8.8
ASN: 15169
AS Name: GOOGLE
Country: US
CIDR: 8.8.8.0/24
----------------------------------------
Host/IP: facebook.com
IP: 157.240.239.35
ASN: 32934
AS Name: FACEBOOK
Country: US
CIDR: 157.240.0.0/16
----------------------------------------
Host/IP: 1.1.1.1
IP: 1.1.1.1
ASN: 13335
AS Name: CLOUDFLARENET
Country: US
CIDR: 1.1.1.0/24
----------------------------------------
```

### Example 2: Using CSV output

```
$ python bulk-whois-lookup.py google.com 8.8.8.8 facebook.com 1.1.1.1 --csv results.csv

Starting bulk Whois lookup...
Results written to results.csv
```

The `results.csv` file will contain:

```
host,ip,asn,as_name,country,cidr
google.com,142.250.180.78,15169,GOOGLE,US,142.250.0.0/15
8.8.8.8,8.8.8.8,15169,GOOGLE,US,8.8.8.0/24
facebook.com,157.240.239.35,32934,FACEBOOK,US,157.240.0.0/16
1.1.1.1,1.1.1.1,13335,CLOUDFLARENET,US,1.1.1.0/24
```

## Error Handling

If a lookup fails for any reason, the script will display an error message for that specific host or IP. In CSV output, failed lookups will have "ERROR" in all fields except the host field.

## Limitations

- The script relies on the accuracy and availability of WHOIS data.
- Some WHOIS servers may rate-limit requests, which could affect bulk lookups of a large number of hosts.
- The script does not handle IPv6 addresses explicitly, though it may work for some IPv6 addresses.
- CIDR range information may not be available for all IP addresses.

## Contributing

Feel free to fork this repository and submit pull requests with any enhancements.

## License

This script is released under the MIT License.