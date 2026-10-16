from django.core.mail import send_mail
from django.conf import settings
def send_activation_email(email,code):
    send_mail(
        subject='Activation your account',
        message=f'emailingiz active qiluvchi code {code}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],


    )
