from django.core.mail import send_mail, send_mass_mail

send_mail(
    'Hola mundo',
    'Probando correo.',
    'miguelmakio61@gmail.com',
    ['miguelmakio61@gmail.com'],
    fail_silently=False,

)