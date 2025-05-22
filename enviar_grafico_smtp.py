import smtplib
import os
from email.message import EmailMessage
from email.utils import make_msgid
from email.mime.image import MIMEImage

# Configura aquí tus datos
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USER = 'tucorreo@gmail.com'
EMAIL_PASS = 'tu_contraseña_o_contraseña_app'
EMAIL_TO = 'destinatario@ejemplo.com'
ASUNTO = 'Gráfico generado con Chart.js'
CUERPO = 'Adjunto el gráfico generado con Chart.js.'

# Ruta al gráfico exportado
PATH_ADJUNTO = 'grafico.png'

def enviar_email():
    # Crear el mensaje
    msg = EmailMessage()
    msg['Subject'] = ASUNTO
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_TO
    msg.set_content(CUERPO)

    # Adjuntar la imagen
    if os.path.exists(PATH_ADJUNTO):
        with open(PATH_ADJUNTO, 'rb') as img:
            img_data = img.read()
            msg.add_attachment(img_data, maintype='image', subtype='png', filename='grafico.png')
    else:
        print("No se encontró el archivo:", PATH_ADJUNTO)
        return

    # Enviar el email por SMTP
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
            print("Correo enviado correctamente.")
    except Exception as e:
        print("Error al enviar correo:", e)

if __name__ == "__main__":
    enviar_email()