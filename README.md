# Domain Information Toolkit

This Python script, the **Domain Information Toolkit**, provides a set of tools to gather information about a domain. It includes the following features:

1. **DNS Lookup**: Performs a DNS lookup for the given domain and displays its associated IP address.

2. **BuiltWith**: Retrieves technology information about the given domain, providing insights into the technologies used to build the website.

3. **GeoIP Lookup**: Uses GeoIP data to provide information about the geographic location of the domain's server.

## Usage



1. **DNS Lookup**:

   Enter a domain (e.g., example.com) when prompted, and the script will perform a DNS lookup to find the associated IP address. It also includes an alternative method that uses an online API to fetch DNS information.

2. **BuiltWith**:

   The script gathers technology information about the domain, revealing the tools and technologies used in the website's construction.

3. **GeoIP Lookup**:

   The script performs a GeoIP lookup using the 'GeoLiteCity.dat' database to identify the geographic location of the server associated with the given domain.

##Prerequisites**:
Before running the script, ensure that you have the required Python libraries installed. You can easily install them using the `requirements.txt` file provided in this repository. Run the following command to install the dependencies:


Install these dependencies using `pip install` if not already installed.

## Example

To run the script, simply execute it, and provide the domain when prompted:

```bash
python domain_info_toolkit.py
```

## Disclaimer

Please use this tool responsibly and respect the privacy and terms of service of the websites and servers you query. Unnecessary or malicious use of this tool may be considered unethical or illegal.
