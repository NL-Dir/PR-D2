from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def get_subscribers(category):
    user_emails = []
    for user in category.subscribers.all():
        user_emails.append(user.email)
    return user_emails


def new_post_mail(instance):
    template = 'mail/new_post.html'

    for category in instance.postCategory.all():
        email_subject = f'New post in category "{category}"!'
        user_emails = get_subscribers(category)

        html = render_to_string(
            template_name=template,
            context={
                'category': category,
                'post': instance,

            }
        )
        msg = EmailMultiAlternatives(
            subject=email_subject,
            body='',
            from_email='info@news.com',
            to=user_emails,
        )

        msg.attach_alternative(html, 'text/html')
        msg.send()
