import qrcode as qr

img= qr.make("https://www.youtube.com/@CyberShieldAcademy1")
img.save("cybershieldacadem.png")


#----------------------
#advanced qr code
#qrcode12.py

from PIL import Image
qr= qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,box_size=10,border=10,)
qr.add_data("https://www.youtube.com/@CyberShieldAcademy1")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("cybershield.png")