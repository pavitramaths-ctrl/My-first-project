import ssl
import socket
from datetime import datetime, UTC

print("==== SSL Certificate Checker ====")

domain = input("Enter website domain (example: google.com): ")

try:
    # Create SSL context
    context = ssl.create_default_context()

    # Connect to website
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:

            # Get SSL certificate
            cert = ssock.getpeercert()

            issuer = dict(x[0] for x in cert['issuer'])
            subject = dict(x[0] for x in cert['subject'])

            valid_from = cert['notBefore']
            valid_until = cert['notAfter']

            print("\n==== SSL Certificate Details ====")
            print("Issuer:", issuer.get('organizationName'))
            print("Issued To:", subject.get('commonName'))
            print("Valid From:", valid_from)
            print("Valid Until:", valid_until)

            # Convert certificate expiry date
            expiry_date = datetime.strptime(
                valid_until,
                "%b %d %H:%M:%S %Y %Z"
            ).replace(tzinfo=UTC)

            # Current UTC time
            current_date = datetime.now(UTC)

            # Calculate days remaining
            days_left = (expiry_date - current_date).days

            print("Days Remaining:", days_left)

            if days_left > 0:
                print("SSL Certificate Status: VALID")
            else:
                print("SSL Certificate Status: EXPIRED")

except Exception as e:
    print("Error:", e)
