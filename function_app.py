import logging
import os
import json
from email.mime.text import MIMEText

from smtplib import SMTP_SSL as SMTP
import azure.functions as func


SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")


app = func.FunctionApp()

@app.service_bus_queue_trigger(arg_name="azservicebus", queue_name="bussin", connection="ServiceBus")
def from_servicebus(azservicebus: func.ServiceBusMessage):
    servicebus_msg: dict = json.loads(azservicebus.get_body().decode('utf-8'))
    logging.info(f"Python ServiceBus Queue trigger processed a message: {servicebus_msg}")

    content = """\
        Newsletter Subscription Confirmation
        Thank you for subscribing to our newsletter!
        """

    msg = MIMEText(content, 'plain')
    msg['Subject'] = "Cloud Newslatter"
    msg['From'] = SMTP_USERNAME

    conn = SMTP('smtp.gmail.com')
    conn.set_debuglevel(1)
    conn.login(SMTP_USERNAME, SMTP_PASSWORD)
    conn.sendmail(SMTP_USERNAME, servicebus_msg["email"], msg.as_string())
    conn.quit()
