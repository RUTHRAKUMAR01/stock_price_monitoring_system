import base64
import functions_framework
import ssl
import smtplib
from email.message import EmailMessage

#Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def hello_pubsub (cloud_event):
    # Print out the data from Pub/Sub, to prove that it worked
    price=float(base64.b64decode(cloud_event.data["message"]["data"]))
    user_price=1400
    if price >= user_price:
        print("message sent")
        email_sender = 'devagcppracise@gmail.com'
        email_password = 'rslv evhg anwy wwuq' # Fetching the password from environment 
        email_receiver = 'sanjeevsan975@gmail.com'
        subiect = 'Alert:Stock Trigger
        body = f"""Dear Investor,
We are writing to inform you that the stock value of Infosys has exceeded the threshold you set in your notificat Given this development, we recommend reviewing your investment strategy and considering any necessary actions in.
Please let us know if you require further assistance or have any questions regarding this alert."""
em=EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)
