import requests
import builtwith
import dns.resolver
import pygeoip

# Domain Input(example.com)
x = input("Enter Domain: ")

print("\n\n"+"*"*100+"\n\n")
print("DNSlookup")

result= requests.get("https://api.hackertarget.com/dnslookup/?q="+x).content.decode("UTF-8")
print(result)


print("*"*100+"\n\n")

# Perform DNS lookup
result = dns.resolver.resolve(x, "A")

# Extract the IP address
for rdata in result:
    domainip = rdata.address

# Print the DNS lookup result
print(f"DNS Lookup Result for {x}:\n{domainip}\n")

print("*" * 100 + "\n\n")

print("Built Tools")
data = builtwith.parse("http://" + x)  # You can also use "https://" if needed
print(data)

print("*" * 100)

# Perform GeoIP lookup
gip = pygeoip.GeoIP('GeoLiteCity.dat')
res = gip.record_by_addr(domainip)
for key, val in res.items():
    print(f'{key}: {val}')
