import getpass
import sqlite3
import argparse
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sys\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', required=True)
args = parser.parse_args()
img = cv2.imread(args.image)

text = pytesseract.image_to_string(img).split()

empval = text.index('#')+1
nameval = text.index('$')+1
designationval = text.index("*")+1

obj = "\nEmployeeCode : "+text[empval]+" || Name : "+text[nameval]+" || DesignationPost : "+text[designationval]
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
