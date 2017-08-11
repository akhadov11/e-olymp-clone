import logging

from django.utils.timezone import now
from django.contrib.auth.backends import ModelBackend

logger = logging.getLogger(__name__)


class AccountMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            try:
                account = user.account
                account.last_activity = now()
                account.save()
            except Exception as ex:
                logger.exception('User does not have account as expected.', extra={
                    'user_id': user.id,
                    'exception': ex
                })
        response = self.get_response(request)
        return response
