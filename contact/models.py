from django.db import models

class Message(models.Model):
    name = models.CharField('Kim jesteś?', max_length=30)
    email = models.EmailField('Twój Email:', null=True, blank=True)
    subject = models.CharField('Temat:', max_length=100)
    message = models.TextField('Wiadomość:')
