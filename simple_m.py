import qrcode
import image
qr=qrcode.QRCode(
    version=10, 
    box_size=10,
    border=4,
)
data="https://www.instagram.com/hamad_marral/"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="black", back_color="white")
img.save("hammad-instagram.png")