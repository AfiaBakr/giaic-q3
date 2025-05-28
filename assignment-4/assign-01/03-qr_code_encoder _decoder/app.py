from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('E:/Governer Generative AI Course/GIAIC Q3/growth_mindset_challenge/assignment-4/assign-01/03-qr_code_encoder _decoder/new/my_qrcode.png')

result = decode(img)

print(result)