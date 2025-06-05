import os
from email.message import EmailMessage
from dotenv import load_dotenv
import smtplib

load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')

def load_template(update_text):
    with open('message_template.txt', 'r') as file:
        template = file.read()
    return template.replace('{{update}}', update_text)

def send_email(subject, content, to='diamondgamerz4949@gmail.com', attachment_path=None):
    email = EmailMessage()
    email['from'] = EMAIL_ADDRESS
    email['to'] = to
    email['subject'] = subject
    email.set_content(content)

    if attachment_path:
        try:
            with open(attachment_path, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(attachment_path)
                email.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
                print(f"📎 Attached: {file_name}")
        except Exception as e:
            print(f"❌ Failed to attach file: {e}")

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(EMAIL_, EMAIL_PASSWORD)
            smtp.send_message(email)
            print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed: {e}")


if __name__ == "__main__":
    try:
        update = input("📝 Enter today's update: ")
        attachment = input("📎 Enter path to attachment (or press Enter to skip): ").strip()

        content = load_template(update)
        print("Debug - Email content:")
        print(content)
        subject = "Daily Report - Update"

        send_email(subject, content, attachment_path=attachment if attachment else None)
    except KeyboardInterrupt:
        print("\n❌ Process interrupted by user.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
