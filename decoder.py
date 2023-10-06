from pyzbar.pyzbar import decode
from PIL import Image
decocdeQR = decode(Image.open(''))  # path of qr code image you want to decode
print(decocdeQR[0].data.decode('ascii'))