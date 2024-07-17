# Bulk Whois Lookup Script

This Python script performs bulk Whois lookups for both hostnames and IP addresses, providing information such as IP address, ASN (Autonomous System Number), AS Name, and associated country.

## Features

- Supports both hostnames and IP addresses
- Performs bulk lookups concurrently for improved efficiency
- Accepts input via stdin, command-line arguments, or interactive input
- Provides detailed error messages for failed lookups

## Prerequisites

Before running the script, make sure you have Python 3.6 or higher installed. You'll also need to install the following Python modules:

```
pip install ipwhois python-whois
```

## Usage

Save the script as `bulk-whois-lookup.py` and use it in one of the following ways:

1. Pipe a list of hostnames or IP addresses:
   ```
   cat hosts.txt | python bulk-whois-lookup.py
   ```

2. Enter hostnames or IP addresses interactively:
   ```
   python bulk-whois-lookup.py
   ```
   Then enter hostnames or IPs, one per line. Press Ctrl+D (Unix) or Ctrl+Z (Windows) to finish.

3. Provide hostnames or IP addresses as command-line arguments:
   ```
   python bulk-whois-lookup.py google.com 8.8.8.8 facebook.com 1.1.1.1
   ```

## Examples

### Example 1: Using a mix of hostnames and IP addresses

```
$ python bulk-whois-lookup.py google.com 8.8.8.8 facebook.com 1.1.1.1

Starting bulk Whois lookup...
Host/IP: google.com
IP: 142.250.180.78
ASN: 15169
AS Name: GOOGLE
Country: US
----------------------------------------
Host/IP: 8.8.8.8
IP: 8.8.8.8
ASN: 15169
AS Name: GOOGLE
Country: US
----------------------------------------
Host/IP: facebook.com
IP: 157.240.239.35
ASN: 32934
AS Name: FACEBOOK
Country: US
----------------------------------------
Host/IP: 1.1.1.1
IP: 1.1.1.1
ASN: 13335
AS Name: CLOUDFLARENET
Country: US
----------------------------------------
```

### Example 2: Piping input from a file

Create a file named `hosts.txt` with the following content:
```
google.com
8.8.8.8
facebook.com
1.1.1.1
```

Then run:
```
$ cat hosts.txt | python bulk-whois-lookup.py
```

The output will be the same as in Example 1.

## Error Handling

If a lookup fails for any reason, the script will display an error message for that specific host or IP. For example:

```
Error for invalid.domain.123: [Errno -2] Name or service not known
```

## Limitations

- The script relies on the accuracy and availability of WHOIS data.
- Some WHOIS servers may rate-limit requests, which could affect bulk lookups of a large number of hosts.
- The script does not handle IPv6 addresses explicitly, though it may work for some IPv6 addresses.

## Contributing

Feel free to fork this repository and submit pull requests with any enhancements.

## License

This script is released under the MIT License.
