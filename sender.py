import requests
import os

def send_simple_message():
    try:
        api_key = os.getenv("MAILGUN_API_KEY")  # Store API key in an env variable
        domain = os.getenv("MAILGUN_DOMAIN")  # Store domain in an env variable
        recipient_email = os.getenv("RECIPIENT_EMAIL")  # Store recipient email

        response = requests.post(
            f"https://api.mailgun.net/v3/{domain}/messages",
            auth=("api", api_key),
            data={
                "from": f"Excited User <mailgun@{domain}>",
                "to": [recipient_email],
                "subject": "Hello",
                "text": "Testing some Mailgun awesomeness!"
            })

        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")

        return response.status_code == 200

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return False

# Call the function
success = send_simple_message()
print(f"Email sent successfully: {success}")
