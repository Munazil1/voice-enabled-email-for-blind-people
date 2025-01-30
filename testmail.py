import requests
import os

url = "https://testmail.app/api/json"

# Fetch API key and recipient email from environment variables
api_key = os.getenv("TESTMAIL_API_KEY")
recipient_email = os.getenv("RECIPIENT_EMAIL")

payload = {
    "to": recipient_email,
    "subject": "Test Email",
    "text": "This is a test email sent using the TestMail API"
}

headers = {
    "X-API-KEY": api_key
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.text)
