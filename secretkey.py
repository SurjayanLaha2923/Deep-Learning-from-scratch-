import secrets
secret_key = secrets.token_hex(16)

print(f"Your Flask app secret key: {secret_key}")