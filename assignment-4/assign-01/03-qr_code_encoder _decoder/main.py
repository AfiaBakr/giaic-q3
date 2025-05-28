import qrcode

data = "This is first QR Code using Python by Afia Bakr"

qr = qrcode.QRCode(version= 1,box_size=10, border=5)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color = 'blue', back_color ='white')

img.save('E:/Governer Generative AI Course/GIAIC Q3/growth_mindset_challenge/assignment-4/assign-01/03-qr_code_encoder _decoder/new/my_qrcode1.png')

