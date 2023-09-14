from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import PostCategory
from .tasks.basic import new_post_mail


@receiver(m2m_changed, sender=PostCategory)
def new_post_notification(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        new_post_mail(instance)