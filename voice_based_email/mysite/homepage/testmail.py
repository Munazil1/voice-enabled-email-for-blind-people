import smtplib

def send_email(subject, body, sender, receiver):
    # SMTP settings for Gmail
    smtp_server = 'smtp.gmail.com'  # Use Gmail's SMTP server
    smtp_port = 587  # Port for STARTTLS encryption

    # Email account credentials for Gmail
    email_username = 'email here'  # Your Gmail email address
    email_password = '16 digit app password'  # Your Gmail app-specific password

    # Compose the email headers and body
    email_message = f"From: {sender}\nTo: {receiver}\nSubject: {subject}\n\n{body}"

    try:
        # Open a secure SMTP connection
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure connection (STARTTLS)
            server.login(email_username, email_password)  # Log in with your Gmail credentials

            # Send the email
            server.sendmail(sender, receiver, email_message)

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error message: {str(e)}")

# Usage example
send_email("Hello from Python", "This is the body of the email.", "munazil.v@seaedu.ac.in", "darkwebber77@gmail.com")
