
import qrcode
# sf =qrcode.make('Sifat Adnan')
# sf.save('sifat.png')

qr = qrcode.QRCode(
   version=1,
    box_size=5,
    border=6
)
qr.add_data("""Name: Sifat Adnan
Occupation:Student(CSE)
University:New Model Degree College
Phone:01621453580
Address:Kamrangirchar ,Dhaka
""")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color='White')
img.save('Sifat_qrCode.png')