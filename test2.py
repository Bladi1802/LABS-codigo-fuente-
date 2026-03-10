import qrcode

# Crear un objeto QR con parámetros específicos
qr = qrcode.QRCode(
    version=1,           # Tamaño (1-40, donde 1 es más pequeño)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Niveles: L, M, Q, H
    box_size=10,         # Tamaño de cada "pixel" del QR en píxeles
    border=4,            # Margen blanco alrededor (mínimo 4)
)

# Agregar datos al QR
qr.add_data('Some data mike')

# Generar el código
qr.make(fit=True)

# Crear imagen con colores personalizados
img = qr.make_image(fill_color="orange", back_color="blue")

# Guardar la imagen
img.save("some_data_mike.png")