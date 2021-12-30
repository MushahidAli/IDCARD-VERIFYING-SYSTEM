# IDCARD VERIFYING SYSTEM
The "IDCARD VERIFYING SYSTEM" uses the Google's latest version of Tesseract OCR[Optical Character Recognition] to recognize and extract meaningful information from an image or a frame image of a webcam while scanning for data-strings present on the image. Once it gets the strings, it searches for specific details by converting it into a list to find EmployeeCode, Name and Designation for the job post and punches them into the "id.db" database file to authenticate the validity of the information that it recently extracted. Once it succeeds in verifies the authentication ladder, it asks to input the user's password, to finalize the verification process.

The main purpose of creating this project is to secure the end user by means of an ID that governs his/her existence over the Grid.

![idcard](https://user-images.githubusercontent.com/30910296/147759161-a819404a-d049-4046-9460-d411ab11dd94.jpg)

# INSTALLATION STEPS-
Before using the code, first make sure you have installed the appropriate Python Libraries! Or else, the code won't execute!

**LIST-**

#1. I'm assuming you are already familiar with the OpenCV Python library used in the Computer Vision Field for images.
(i.e., ```pip install opencv-contrib-python```) - Pre-built CPU-only OpenCV package.

#2. Install pytesseract python library using the pip command! This package is used to extract data-strings or meaningful information from a given image!
Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images.
(i.e., ```pip install pytesseract```) - This command tries to download either (.whl - wheel file) or (.tar.gz - tar ball file) from https://pypi.org/project/pytesseract/#files

#3. And then finally, install a 32 based or 64 based tesseract binary executable from https://digi.bib.uni-mannheim.de/tesseract/ or just download this one(x64) - https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20210811.exe

#4. Find the location of the tesseract.exe file in here - C:\Users\sys\AppData\Local\Programs\Tesseract-OCR and then make this link : [[ C:\Users\sys\AppData\Local\Programs\Tesseract-OCR\tesseract.exe ]]. You should include this link in .PY python running files based on your own requirement or else, it won't work!

#NOTE : Include the tesseract.exe location in your python scripts!

EG : ``` pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sys\AppData\Local\Programs\Tesseract-OCR\tesseract.exe' ```

# HOW TO USE IT-

There are 2 files [webcam.py && without_webcam.py]

a. webcam.py - This py script will run using a webcam to screenshot the image of your ID CARD for authentication purpose! Please do try to take a clear image or else it won't work!

b. without_webcam.py - This py script will run using arguments such as **-i OR --image** along with the image location!

USAGE: ```python without_webcam.py -i id_cards/idcard.jpg```

OR

USAGE: ```python without_webcam.py --image id_cards/idcard.jpg```

You will be provided with 3 ID's to test the AI application, out of which one of them is fake(fakeidcard.jpg)!

**For idcard.jpg, the password is "UIDHYUIQ123" and for idcard1.jpg, the password is "GGQUIHGY123"**

# AUTHENTICATION-

It's pretty simple! The Tesseract OCR extracts credentials from a card and scans for vital details that can be punched in using sqlite3 to verify whether you're a real or a fake user. The next and last step is to verify the user's integrity through the means of a login_passcode to finalize the authentication!
