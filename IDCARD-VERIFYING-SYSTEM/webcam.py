import getpass
import sqlite3
import os
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sys\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

cap = cv2.VideoCapture(0)
while True:
    return_value,image = cap.read()
    cv2.imshow('INPUT - Press S To ScreenShot!',image)
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite('screenshotimage.jpg',image)
        break

cap.release()
cv2.destroyAllWindows()

img = cv2.imread("screenshotimage.jpg")
os.remove("screenshotimage.jpg")
text = pytesseract.image_to_string(img).split()

try:
  empval = text.index('#')+1
except:
  os.system("cls")
  print("Image Was Unclear!\nPlease Try Again!")
  exit()

os.system("cls")

if len(str(text[empval])) == 8:
  print("Verifying..")
else:
  print("Please Try Again!\nImage Was Unclear!")
  exit()

obj = "\nEmployeeCode : "+text[empval]
print(obj)

connection = sqlite3.connect("id.db")
cursor = connection.cursor()
rows = cursor.execute(" SELECT EmployeeCode FROM ID WHERE EmployeeCode='"+text[empval]+"' ").fetchall()
print("\nSearching the dB..\n")
try:
  print(rows[0])
except:
  print("This Employee_ID Doesn't Even Exist In Own Database!")
  exit()

passcode = str(getpass.getpass(prompt='Enter The Password: ', stream=None))
valueCode = cursor.execute(" SELECT EmployeeCode FROM ID WHERE EmployeeCode='"+text[empval]+"' AND Password='"+passcode+"' ").fetchall()
try:
  print(valueCode[0])
except:
  print("\nUnauthorized Identity!")
  exit()

print("Verified Identity!")
