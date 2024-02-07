import requests

def validate_license(user_email, license_key, hardware_id):
    # URL of your Flask server
    server_url = "http://localhost:5000/validate_license"  # Replace with your server URL

    # Data to be sent in the request body
    data = {
        "email": user_email,
        "license_key": license_key,
        "hardware_id": hardware_id
    }

    # Send an HTTP POST request to the server
    response = requests.post(server_url, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the validation result from the response
        validation_result = response.json()
        return validation_result
    else:
        # Print an error message if the request failed
        print("Error:", response.text)
        return None

# Example usage
if __name__ == "__main__":
    user_email = input("Enter your email: ")
    license_key = input("Enter your license key: ")
    hardware_id = input("Enter your hardware ID: ")
    
    validation_result = validate_license(user_email, license_key, hardware_id)
    if validation_result:
        if validation_result["valid"]:
            print("License key is valid.")
        else:
            print("License key is invalid.")
    else:
        print("Failed to validate license key.")
