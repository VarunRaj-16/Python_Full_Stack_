print("7. EMAIL SENDING PROJECT (Demo Structure)")
import smtplib        # Required setup:   # 1. Enable 2-Step Verification on Gmail          # 2. Generate App Password from Google Account
from email.message import EmailMessage
sender_email = 'varunrajvarakala16@gmail.com'
receiver_email = 'shivatejaarva25@gmail.com'
app_password = 'cfum cbmr jvrh qvjg'
msg = EmailMessage()
msg['Subject'] = 'Meeting Reminder'
msg['From'] = sender_email
msg['To'] = receiver_email
msg.set_content('''Hi,
Just reminding you about our meeting tomorrow at 10 AM.
Regards,
Varun''')
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)
        print("Email sent successfully!")
except Exception as e:
    print("Error:", e)
