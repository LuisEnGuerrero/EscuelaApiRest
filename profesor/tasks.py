from django.core.mail import send_mail
from Escuela.celery import app


@app.task(name='send_email')
def send_email(emails, nombre):
    send_mail(
        subject='Bienvenido a nuestra Institución!',
        message=f'Apreciado Profesor: {nombre} para nuestra institucion es muy grato darle la bienvenida.',
        from_email='admin@escuela.com',
        recipient_list=emails,
        html_message=f'<h1>Bienvenido a esta institución:</h1><h2>Apreciado: {nombre}</h2>'

    )