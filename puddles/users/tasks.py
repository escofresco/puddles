import json
from django.contrib.auth import get_user_model

from config import celery_app

User = get_user_model()


@celery_app.task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()

@celery_app.task()
def pretty_print_response(response):
    print(json.dumps(response, indent=2, sort_keys=True))