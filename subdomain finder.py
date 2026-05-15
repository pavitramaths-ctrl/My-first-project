import requests

domain = input("Enter Domain (example.com): ")

try:
    with open("subdomains.txt", "r") as file:

        for subdomain in file:

            subdomain = subdomain.strip()

            url = f"https://{subdomain}.{domain}"

            try:
                response = requests.get(url, timeout=3)

                if response.status_code < 400:
                    print(f"[+] Found: {url}")

            except requests.ConnectionError:
                pass

            except requests.Timeout:
                print(f"[-] Timeout: {url}")

except FileNotFoundError:
    print("Error: subdomains.txt file not found!")
