import datetime
from django.conf import settings
from django.contrib.auth.models import AbstractUser, models
from django.db.models import CharField, IntegerField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
import plaid
from .tasks import pretty_print_response


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    score = IntegerField(_("Credit Score"), default=0)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class PlaidToken(models.Model):
    access_token = models.CharField(max_length=64, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class BankTransaction(models.Model)


class BankAccount(models.Model):

    raw = CharField()
    transactions = 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # # Retrieve Transactions for an Item
    # # https://plaid.com/docs/#transactions
    # def get_transactions(self):
    #     # Pull transactions for the last 30 days

    #     client = plaid.Client(client_id=PLAID_CLIENT_ID,
    #                         secret=PLAID_SECRET,
    #                         environment=PLAID_ENV,
    #                         api_version='2019-05-29')
    #     start_date = '{:%Y-%m-%d}'.format(datetime.datetime.now() + datetime.timedelta(-30))
    #     end_date = '{:%Y-%m-%d}'.format(datetime.datetime.now())
    #     try:
    #         transactions_response = client.Transactions.get(self.user.access_token, start_date, end_date)
    #     except plaid.errors.PlaidError as e:
    #         return self.format_error(e)
    #     pretty_print_response(transactions_response)
    #     return transactions_response

    # def format_error(self, e):
    #     return {'error': {'display_message': e.display_message, 'error_code': e.code, 'error_type': e.type, 'error_message': e.message } }
