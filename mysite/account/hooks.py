import hashlib
import random

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .tasks import send_async_mail_task


def send_confirmation_email(to, ctx, sender=settings.DEFAULT_FROM_EMAIL):
    """Send an email with a link for email address confirmation.

    Args:
        to (list of str): Recipient list (email addresses).
        ctx: (dict): Context to pass to an email template.
        sender (str): Sender email address.
    """
    subject = render_to_string('account/email/email_confirmation_subject.txt', ctx)
    subject = ''.join(subject.splitlines())  # remove superfluous line breaks
    message = render_to_string('account/email/email_confirmation_message.txt', ctx)
    html_message = render_to_string('account/email/email_confirmation_message.html', ctx)
    send_async_mail_task.delay(subject, message, sender, to, html_message=html_message)


def send_password_reset_email(to, ctx, sender=settings.DEFAULT_FROM_EMAIL):
    """Send an email with a link for password resetting.

    Args:
        to (list of str): Recipient list (email addresses).
        ctx: (dict): Context to pass to an email template.
        sender (str): Sender email address.
    """
    subject = render_to_string("account/email/password_reset_subject.txt", ctx)
    subject = "".join(subject.splitlines())
    message = render_to_string("account/email/password_reset.txt", ctx)
    html_message = render_to_string('account/email/password_reset.html', ctx)

    message = message + "\nPassword Reset URL: {}".format(ctx['password_reset_url'])
    send_mail(subject, message, sender, to, html_message=html_message, fail_silently=False)

    # send_async_mail_task.delay(subject, message, sender, to)


def send_password_change_email(to, ctx, sender=settings.DEFAULT_FROM_EMAIL):
    """Send an email to notify about password changing.

    Args:
        to (list of str): Recipient list (email addresses).
        ctx: (dict): Context to pass to an email template.
        sender (str): Sender email address.
    """
    subject = render_to_string("account/email/password_change_subject.txt", ctx)
    subject = "".join(subject.splitlines())
    message = render_to_string("account/email/password_change.txt", ctx)
    send_async_mail_task.delay(subject, message, sender, to)


def generate_random_token(extra=None, hash_func=hashlib.sha256):
    """Generate random token.

    Args:
        extra (list of str): Some extra salt.
        hash_func: Hash function.

    Returns:
        str: New token, 64 characters.
    """
    if extra is None:
        extra = []
    bits = extra + [str(random.SystemRandom().getrandbits(512))]
    return hash_func("".join(bits).encode("utf-8")).hexdigest()


def generate_signup_code_token(email=None):
    """Generate signup token. Email can be user as additional salt.

    Args:
        email (str or None): Email

    Returns:
        str: New token, 64 characters.
    """
    extra = []
    if email:
        extra.append(email)
    return AccountDefaultHookSet.generate_random_token(extra)


def generate_email_confirmation_token(email):
    """Generate email confirmation token.

    Args:
        email (str): Email address.

    Returns:
        str: New token, 64 characters.
    """
    return generate_random_token([email])


def generate_file_token(self, file):
    """Generate file token.

    Args:
        file (str): File name.

    Returns:
        str: New token, 64 characters.
    """
    return self.generate_random_token([file])
