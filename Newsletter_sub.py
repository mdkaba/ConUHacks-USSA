from twilio.rest import Client
import datetime as dt
from main import *


def sending_newsletter(user_email):
    import smtplib

    my_email = "adamosayinghi@gmail.com"
    password = "tqlfrjigxyetsixn"

    # Yahoo: smtp.mail.yahoo.com (SMTP info)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # tls: Transport Layer Security
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=user_email,
                            msg="Subject:Hello student\n\nWelcome to the USSA community! We're thrilled to have you on board, ready to embark on a monthly journey of learning marvels.\nThank you for subscribing to our monthly newsletter – your passport to a world of personalized tips, resources, and programs designed with you in mind. 🚀✨\nWhat to Expect:\n📆 Monthly Learning Highlights:\nOnce a month, we'll be dropping into your inbox with a roundup of the latest learning insights, tailored just for you. Expect a curated collection of tips and tricks to spice up your study routine.\n🌟 Exclusive Monthly Features:\nDive into exclusive monthly features that delve deep into various learning styles. Whether you're a visual explorer, an auditory adventurer, or a kinesthetic journeyer, we've got you covered with content that speaks directly to your learning profile.\n📚 Resource Spotlight:\nUncover valuable resources handpicked to amplify your learning experience. From articles and guides to recommended tools, each month brings a new spotlight on resources that align with your learning needs.\n🎓 Community Connection:\nConnect with your fellow learners in our vibrant community. Engage in discussions, share your discoveries, and be part of a supportive community that understands and celebrates diverse learning styles.\nNext Steps:\nGet ready for your first monthly marvel, set to arrive in your inbox shortly! In the meantime, feel free to explore [Your Learning App] and make the most of the features designed to enhance your learning adventure.\nHave questions, thoughts, or stories to share? We're all ears! Reach out to us at [support@ussa.com] – we'd love to hear from you.\nThank you for choosing USSA. We're excited to be a part of your monthly learning experience!\nHappy learning!\nBest regards,\nThe USSA team")

def activate_newsletter(user_email):
    months_in_a_year = 1
    testing_time = dt.datetime(year=dt.datetime.now().year, month=dt.datetime.now().month, day=1)
    while months_in_a_year != 12:
        if testing_time == dt.datetime.now():
            sending_newsletter(user_email)
            months_in_a_year -= 1

# account_sid = "AC7c86b3e0c201bde277a8b74c7646350d"
# auth_token = "19898c10d58a8626f388bb7d8a8aad80"
#
# message = "It's going to rain today :'("
#
# client = Client(account_sid, auth_token)
# message = client.messages \
#         .create(
#         body=message,
#         from_='+15854878959',
#         to='+1 514 963 1025' # user input
#     )
