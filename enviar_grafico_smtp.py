import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Configuración SMTP (modifica según tu proveedor)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USER = 'tucorreo@gmail.com'
EMAIL_PASS = 'tu_contraseña_app'
EMAIL_TO = 'destinatario@ejemplo.com'
ASUNTO = 'Varios Gráficos Chart.js incrustados en HTML'

# Lista de imágenes a incrustar
imagenes = [
    ('grafico1.png', 'grafico1'),
    ('grafico2.png', 'grafico2'),
    ('grafico3.png', 'grafico3'),
]

# Construimos el HTML referenciando las imágenes por su Content-ID
html = """
<html>
  <body>
    <h2>Gráficos generados con Chart.js</h2>
    <p>Primer gráfico:</p>
    <img src="cid:grafico1"><br>
    <p>Segundo gráfico:</p>
    <img src="cid:grafico2"><br>
    <p>Tercer gráfico:</p>
    <img src="cid:grafico3"><br>
  </body>
</html>
"""

def enviar_email():
    msg = MIMEMultipart('related')
    msg['Subject'] = ASUNTO
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_TO

    msg_alt = MIMEMultipart('alternative')
    msg.attach(msg_alt)
    msg_alt.attach(MIMEText("Tu cliente de correo no soporta HTML.", 'plain'))
    msg_alt.attach(MIMEText(html, 'html'))

    # Adjuntar cada imagen como parte del email, referenciando su Content-ID
    for img_path, cid in imagenes:
        with open(img_path, 'rb') as f:
            img = MIMEImage(f.read())
            img.add_header('Content-ID', f'<{cid}>')
            img.add_header('Content-Disposition', 'inline', filename=img_path)
            msg.attach(img)

    # Enviar el email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)
        print('Correo enviado correctamente.')

if __name__ == "__main__":
    enviar_email()
