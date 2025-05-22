import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Configuración SMTP
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USER = 'tucorreo@gmail.com'
EMAIL_PASS = 'tu_contraseña_app'
EMAIL_TO = 'destinatario@ejemplo.com'
ASUNTO = 'Tablero de Contracargo - Gráficos embebidos'

# Lista de nombres de archivos y content IDs
canvas_imgs = [
    ('myChart.png', 'myChart'),
    ('myChart2.png', 'myChart2'),
    ('myChart3.png', 'myChart3'),
    ('myChart4.png', 'myChart4'),
    ('myChart5.png', 'myChart5'),
    ('myChart6.png', 'myChart6'),
    ('myChart7.png', 'myChart7'),
    ('myChart8.png', 'myChart8'),
    ('myChart9.png', 'myChart9'),
]

# Construye el HTML del email con las imágenes embebidas
html = """
<html>
  <body>
    <h2>Tablero de Contracargo BPS</h2>
    <p><b>Gráfico 1</b></p><img src="cid:myChart"><br>
    <p><b>Gráfico 2</b></p><img src="cid:myChart2"><br>
    <p><b>Gráfico 3</b></p><img src="cid:myChart3"><br>
    <p><b>Gráfico 4</b></p><img src="cid:myChart4"><br>
    <p><b>Gráfico 5</b></p><img src="cid:myChart5"><br>
    <p><b>Gráfico 6</b></p><img src="cid:myChart6"><br>
    <p><b>Gráfico 7</b></p><img src="cid:myChart7"><br>
    <p><b>Gráfico 8</b></p><img src="cid:myChart8"><br>
    <p><b>Gráfico 9</b></p><img src="cid:myChart9"><br>
  </body>
</html>
"""

def enviar_email():
    msg = MIMEMultipart('related')
    msg['Subject'] = ASUNTO
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_TO

    alt = MIMEMultipart('alternative')
    msg.attach(alt)
    alt.attach(MIMEText("Tu cliente de correo no soporta HTML.", 'plain'))
    alt.attach(MIMEText(html, 'html'))

    for filename, cid in canvas_imgs:
        try:
            with open(filename, 'rb') as f:
                img = MIMEImage(f.read())
                img.add_header('Content-ID', f'<{cid}>')
                img.add_header('Content-Disposition', 'inline', filename=filename)
                msg.attach(img)
        except Exception as e:
            print(f"No se pudo adjuntar {filename}: {e}")

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)
        print('Correo enviado correctamente.')

if __name__ == "__main__":
    enviar_email()
