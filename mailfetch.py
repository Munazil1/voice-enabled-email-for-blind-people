import getpass
import imaplib
import email

def fetch_emails(username, password, sender=None, subject=None):
    # create an IMAP4_SSL instance and login
    server = 'imap.gmail.com'
    imap = imaplib.IMAP4_SSL(server)
    
    try:
        # Attempt to login
        imap.login(username, password)
        print("Login successful!")
    except imaplib.IMAP4.error as e:
        print(f"Login failed: {e}")
        print("Note: For Gmail, you need to use an App Password if 2FA is enabled")
        return []

    # select the INBOX mailbox
    imap.select('INBOX')

    # search for messages that match the specified criteria
    criteria = ['ALL']
    if sender:
        criteria.append('FROM "{}"'.format(sender))
    if subject:
        criteria.append('SUBJECT "{}"'.format(subject))
    search_criteria = ' '.join(criteria)
    
    try:
        typ, data = imap.search(None, search_criteria)
        if typ != 'OK':
            print("Search failed")
            return []

        # loop through the list of message IDs returned by the search
        messages = []
        for msg_id in data[0].split():
            # fetch the message by ID
            typ, msg_data = imap.fetch(msg_id, '(RFC822)')
            if typ == 'OK':
                # convert the message data to an EmailMessage object
                msg = email.message_from_bytes(msg_data[0][1])
                messages.append(msg)

    except Exception as e:
        print(f"Error fetching messages: {e}")
        messages = []
    finally:
        # close the mailbox and logout
        imap.close()
        imap.logout()

    return messages

if __name__ == "__main__":
    # prompt the user for their Gmail credentials
    username = input('Enter your Gmail address: ')
    password = getpass.getpass('Enter your App Password: ')

    # fetch emails from the inbox
    emails = fetch_emails(username, password)

    # print the subjects of the fetched emails
    if emails:
        for email_msg in emails:
            print('Subject:', email_msg['Subject'])
    else:
        print("No emails found.")
