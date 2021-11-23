from django.core.mail import send_mail
from Escuela.celery import app


@app.task(name='send_email')
def send_email(emails, nombre):
    send_mail(
        subject='Hay una nueva tarea publicada para tu Grupo',
        message=f'Se ha publicado una nueva tarea con titulo: {nombre} para tu grupo de estudio',
        from_email='admin@escuela.com',
        recipient_list=emails,
        html_message=f'<h1>Nueva Tarea Asignada a tu Grupo</h1><h2>Título: {nombre}</h2>'

    )