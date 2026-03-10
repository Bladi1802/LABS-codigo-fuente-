import qrcode
import os

# Crear carpeta si no existe
os.makedirs('qr_codes', exist_ok=True)

# Lista de datos para generar QRs
datos = [
    'https://github.com',
    'https://google.com',
    'https://python.org',
    'https://wikipedia.org',
    'https://stackoverflow.com',
]

# Generar QRs
for i, url in enumerate(datos, 1):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f'qr_codes/qr_{i}.png')
    print(f"✓ QR {i} creado: {url}")

print("\n✓ Todos los QRs fueron creados en la carpeta 'qr_codes/'")
