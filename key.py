import hashlib
import base64

def generate_license_key(user_email, secret_salt):
    # Create a unique license key based on the user's email and a secret salt
    hash_object = hashlib.sha256(user_email.encode() + secret_salt.encode())
    license_key = base64.urlsafe_b64encode(hash_object.digest()).decode('utf-8')
    return license_key

# Example usage
user_email = "user@example.com"
secret_salt = "YourSecretSaltHere"
license_key = generate_license_key(user_email, secret_salt)
print("Generated License Key:", license_key)
