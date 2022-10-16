
#                ------- A Simple python program to generate qr code of a given link----------



# first you have to install "pyqrcode" library
# just open your commandline and type "pip install pyqrcode"
import pyqrcode 
from pyqrcode import QRCode 
from PIL import Image
  
# Taking input of the String which represent the QR code 
s = input("Enter the link:\n")
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.png("myqr.png", scale = 8) 

