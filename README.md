# Keylogger
This has a keylogger created by me which can be packaged in anything, any file you want and by social engineering you can use it. <br />
This keylogger sends feedback via email and it sends the key pressed as well as a screenshot of the victim pc in a certain time interval. <br /> <br />
How to use: <br /><br />
So to use this as python file its all ready but to package it into image or anything you have to use 'pyinstaller' script which you can download via pip. <br />
And at this time I am using pyinstaller==3.5 (version) that is running errorless for me. <br />
To package this into image/pdf/anything you have to first edit the 'Keylogger.py' file and erase the '#' in line 25   i.e. '#self.check_file()' --> 'self.check_file()' <br />
For more info on pyinstaller visit 'https://pyinstaller.readthedocs.io/en/stable/usage.html'<br />
