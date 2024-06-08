# run CMD or Terminal to install required module 
# pip install pyqrcode 
# pip install pypng
import pyqrcode 
import png 
from pyqrcode import QRCode 
# inputData which represents the input information 
inputData = str(input("copy paste your information  here-->>"))
# Generate QR code with saved info as in above variable name qrcode 
qrcode= pyqrcode.create(inputData) 
# Create and save the svg file naming "mysvgfile.svg" 
#qrcode.svg("mysvgfile.svg", scale = 8) 
#svg file is scalable vector 2D graphic file Which contains the Quality of graphic
# Create and save the png file naming "QRcode.png" 
qrcode.png('QRcode.png', scale = 6) 
