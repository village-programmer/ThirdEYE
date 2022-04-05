import sys
sys.path.append('../')
import requests
from playsound import playsound
from Databases.database import AuthenticationDatabase, SettingsDatabase
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


"""
    Alert system 2.1
    By Vikas Patel @ DTech 
    www.villageprogrammer.tech   
"""
class Alert:
    __url = "https://www.fast2sms.com/dev/bulk"
    __headers = None
    def __init__(self):
        db = AuthenticationDatabase()
        self.sdb = SettingsDatabase()
        self.__headers = db.authentication_data()
        db.con.close()
        self.number = self.sdb.get_mobile()
        self.receiver = self.sdb.get_email()
        message =  self.sdb.get_message()
        message = message.replace(" ","%20")
        self.message = message

        self.__payload = "sender_id=FSTSMS&message="+self.message+"&language=english&route=p&\
        numbers="+self.number


    def set_message(self,message):
        message = message.replace(" ","%20")
        self.message = message

    def set_number(self,number):
        self.number = str(number)

    def alertSound(self):
        # print("playing sound")
        playsound("Assets/Sound/alert_sound.mp3")

    def alertSMS(self):
        response = requests.request("POST", self.__url, data=self.__payload, headers=self.__headers)
        print(response.text)

    def printd(self):
        print(self.__headers)

        
    def send_email(self):
        file = open("Alert/loginfile.txt", "r")
        intruder_file = "INTRUDER.png"

        login = []
        for line in file:
            login.append(line)
        file.close()
        email_user = login[0]  # sender account
        email_password = login[1]  # sender password
        email_send = self.receiver  # receiver account

        subject = "Third Eye Alert: Security Breach"

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        body = "Security Breach at your home"
        msg.attach(MIMEText(body, 'plain'))
        attachment = open(intruder_file, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + intruder_file)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        print("Starting server...")
        server.starttls()
        print("Logging in...")
        server.login(email_user, email_password)
        print("Sending Email...")
        server.sendmail(email_user, email_send, text)

        print("Email sent.")
        server.quit()

# a = Alert()
# a.printd()
# a.alertSound()
