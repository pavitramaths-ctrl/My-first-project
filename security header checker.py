import requests

# Banner
print("=" * 50)
print("      SECURITY HEADER CHECKER")
print("=" * 50)

# Get website URL
url = input("\nEnter Website URL: ")

try:
    # Send request
    response = requests.get(url)

    # Security headers list
    security_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-XSS-Protection",
        "X-Content-Type-Options",
        "Referrer-Policy"
    ]

    print("\nChecking Security Headers...\n")

    # Save results
    file = open("results.txt", "w")

    # Check headers
    for header in security_headers:

        if header in response.headers:
            result = f"[FOUND] {header} : {response.headers[header]}"
            print(result)
            file.write(result + "\n")

        else:
            result = f"[MISSING] {header}"
            print(result)
            file.write(result + "\n")

    file.close()

    print("\nScan Completed!")
    print("Results saved in results.txt")

except requests.exceptions.RequestException:
    print("Connection Error!")
