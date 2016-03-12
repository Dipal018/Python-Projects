from twilio.rest import TwilioRestClient

account_sid = "AC4c9770fb31e809c3cb8de009c332759f"
auth_token = "87a447fd9e486f539880cd0b6d572f51"
client = TwilioRestClient(account_sid,auth_token)

message = client.sms.messages.create(
    body="Hello Dipal... I am learning python.",
    to="+16692548594",
    from_="+14695182751")

print message.sid
