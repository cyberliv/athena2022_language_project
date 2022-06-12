"""
Utilities for tests.py usage.

"""

from django.conf import settings
from django.core.mail import send_mail

class UserRepresentation:
    "POSTMAN_SHOW_USER_AS = 'postman.module_for_tests.UserRepresentation'"
    def __init__(self, user):
        self.user = user

    def __str__(self):
        return user_representation(self.user)


def user_representation(user):
    "POSTMAN_SHOW_USER_AS = 'postman.module_for_tests.user_representation'"
    return 'nick_' + user.get_username()  # some user representation


def notification_approval(user, action, site):
    return '{}_{}@domain.tld'.format(user.username, action)  # a way to prove at the same time the parameters transmission


def send(users, label, extra_context):
    "POSTMAN_NOTIFIER_APP = 'postman.module_for_tests'"
    send_mail('subject', 'message', settings.DEFAULT_FROM_EMAIL, [users[0].email])