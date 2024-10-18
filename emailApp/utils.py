from django.core.mail import send_mail


def send_email(to, subject, from_, body):
    try:
        send_mail(
            subject=subject,
            message=body,
            from_email=from_,
            recipient_list=[to],
            fail_silently=False
        )

        print("Email sent successfully")

    except Exception as e:
        print(e)
