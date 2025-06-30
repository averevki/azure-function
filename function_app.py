import logging
import os
import json

# import msal
# import requests
import azure.functions as func
import azure.servicebus as servicebus


app = func.FunctionApp()


# def main(msg: func.ServiceBusMessage):
#     email = msg.get_body().decode('utf-8')
#     logging.info(f"Processing: {email}")
#
#     # Get credentials from environment
#     client_id = os.environ["CLIENT_ID"]
#     client_secret = os.environ["CLIENT_SECRET"]
#     tenant_id = os.environ["TENANT_ID"]
#     mail_username = os.environ["MAIL_USERNAME"]
#
#     # Get Microsoft Graph token
#     app = msal.ConfidentialClientApplication(
#         client_id,
#         authority=f"https://login.microsoftonline.com/{tenant_id}",
#         client_credential=client_secret
#     )
#     token = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
#
#     if "access_token" in token:
#         send_email(token["access_token"], email, mail_username)
#     else:
#         logging.error(f"Token acquisition failed: {token.get('error')}")
#
#
# def send_email(access_token, recipient, sender):
#     url = f"https://graph.microsoft.com/v1.0/users/{sender}/sendMail"
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Content-Type": "application/json"
#     }
#
#     email_body = {
#         "message": {
#             "subject": "Welcome to Our Newsletter!",
#             "body": {
#                 "contentType": "Text",
#                 "content": "Thank you for subscribing...\n\nUnsubscribe: https://example.com/unsubscribe"
#             },
#             "toRecipients": [{"emailAddress": {"address": recipient}}]
#         }
#     }
#
#     response = requests.post(url, headers=headers, json=email_body)
#     if response.status_code == 202:
#         logging.info(f"Email sent to {recipient}")
#     else:
#         logging.error(f"Email failed: {response.text}")


@app.function_name(name="servicebus_trigger")
@app.service_bus_queue_trigger(arg_name="azservicebus", queue_name="bussin", connection="ServiceBus")
def servicebus_trigger(azservicebus: servicebus.ServiceBusReceivedMessage):
    logging.info(f"Python ServiceBus Queue trigger processed a message: {azservicebus.body}")
