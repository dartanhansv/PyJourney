import socket

# Ask the user for a website URL
website_url = input("Enter a website URL (e.g., example.com): ")

try:
    # Get the IP address of the website
    ip_address = socket.gethostbyname(website_url)
    print(f"The IP address of {website_url} is: {ip_address}")
except socket.gaierror:
    print("Invalid URL or unable to resolve the IP address.")
