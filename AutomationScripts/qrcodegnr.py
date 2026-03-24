#generate QR code for the given data

import qrcode

data = input("Enter a link or a text: ")

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save("sample.png") #name of the img

print("QR code generated successfully and saved as sample.png")