import qrcode

qrText = input("Введите текст который необходимо повестистить в qrcode: \n")
fileName = input("Введите имя файла для сохранения: \n")

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data(qrText)

img = qr.make_image()
img.save(f"images/{fileName}.png")