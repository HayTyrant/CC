import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    # Your email credentials and SMTP server information
    sender_email = 'your_email@gmail.com'  # replace with your email address
    sender_password = 'your_email_password'  # replace with your email password
    smtp_server = 'smtp.gmail.com'  # replace with your SMTP server

    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message.as_string())

# Example condition (replace this with your actual condition)
if some_condition_is_true:
    send_email("Fraud Alert", "Your credit card transaction is fraudulent.", "recipient@example.com")
