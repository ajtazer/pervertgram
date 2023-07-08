from instagram_private_api import Client
import requests
import getpass

def login(username, password):
    otp_code = "674951"  # Replace with the actual OTP code
    api = Client(username, password)
    try:
        api.two_factor_login(verification_code=otp_code)
    except ClientError as e:
        if e.code == 'two_factor_required':
            raise ValueError("Invalid one-time password (OTP).")
        else:
            raise e
    return api


api = login(username, password)

def login(username, password):
    api = Client(username, password)
    return api

api = login(username, password)

# Example: Fetch user details
user_id = api.authenticated_user_id
user_info = api.user_info(user_id)
print(user_info)
