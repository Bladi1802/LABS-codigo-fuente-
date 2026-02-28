# LIBRERIAS
from os import name

import qrcode
from faker import Faker

#VARIABLES y CONSTANTES
fake = Faker()

#flujo del programa
for _ in range(10):
    name = fake.name()
    img = qrcode.make(name)
    img.save(name + ".png")
    print(f"QR code for {name} generated and saved as {name}.png")


