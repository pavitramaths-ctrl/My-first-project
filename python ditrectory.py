import requests

# Target website
url = input("Enter website URL: ")

# Common directories
directories = [
    "admin",
    "login",
    "dashboard",
    "wp-admin",
    "cpanel",
    "uploads",
    "images"
]

print("\nChecking directories...\n")

for directory in directories:
    target_url = f"{url}/{directory}"

    try:
        response = requests.get(target_url)

        if response.status_code == 200:
            print(f"[FOUND] {target_url}")
        else:
            print(f"[NOT FOUND] {target_url}")

    except requests.exceptions.RequestException:
        print(f"[ERROR] Could not connect to {target_url}")
        print(target_url, response.status_code)
        import requests

url = input("Enter website URL: ")

directories = [
    "admin",
    "login",
    "dashboard",
    "wp-admin",
    "cpanel",
    "uploads",
    "images"
]

print("\nChecking directories...\n")

for directory in directories:

    target_url = f"{url}/{directory}"

    try:
        response = requests.get(target_url)

        print(f"{target_url} --> Status Code: {response.status_code}")

    except:
        print("Connection Error")
