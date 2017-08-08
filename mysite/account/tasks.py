import logging

from django.core.mail import send_mail

logger = logging.getLogger(__name__)


def send_async_mail_task(subject, message, from_email, recipient_list, **kwargs):
    """Celery task with exactly the same interface as send_mail. Just encapsulates send_mail."""
    send_mail(subject, message, from_email, recipient_list, **kwargs)
