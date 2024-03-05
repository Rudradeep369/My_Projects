# To send a message on WhatsApp using Python, you need to use the Twilio API. Here is a basic example of how you can do it:

# First, you need to sign up for a Twilio account and get a Twilio phone number.
# Install the Twilio Python library by running the following command in your terminal: pip install twilio
# Create a new Python file and import the following modules:

# from twilio.rest import Client

# # Your Account Sid and Auth Token from twilio.com/console
# account_sid = 'your_twilio_account_sid'
# auth_token = 'your_twilio_auth_token'
# client = Client(account_sid, auth_token)

# # Your Twilio number and the number you want to send the message to
# from_whatsapp_number = 'whatsapp:+14155238886'
# to_whatsapp_number = 'whatsapp:+1234567890'

# # The message you want to send
# message = client.messages.create(
#     body='Hello, there!',
#     from_=from_whatsapp_number,
#     to=to_whatsapp_number
# )

# print(message.sid)
# Note that you need to replace the placeholder values in the code with your actual Twilio account SID and auth token, as well as the Twilio number you want to send the message from and the number you want to send the message to.

# This code will send the message "Hello, there!" from your Twilio number to the specified WhatsApp number. The message SID will be printed after the message is sent.





# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



# import pywhatkit
# number=input()
# message=input()
# hr=input()
# min=input()
 
# # pywhatkit.sendwhatmsg("+919830141522", "Hello sir", 17, 29)

# pywhatkit.sendwhatmsg( number, message, hr, min)


import pywhatkit

# Take user input for the message text
message_text = input("Enter the message text: ")

# Take user input for the phone number
phone_number = input("Enter the phone number (in international format): ")

# Take user input for the hour and minute to send the message
hour = int(input("Enter the hour (24-hour format): "))
minute = int(input("Enter the minute: "))

# Use pywhatkit to send the message at the specified time
pywhatkit.sendwhatmsg(phone_number , message_text, hour, minute)

print("Message sent successfully!")