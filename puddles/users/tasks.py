from django.contrib.auth import get_user_model

from config import celery_app

User = get_user_model()


@celery_app.task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()

@celery_app.task()
def invoke_knime_creditscore_predictor_endpoint():
    """A celery task to invoke the Knime Credit Score Predictor from the AWS
    Marketplace"""
    raise NotImplemented
