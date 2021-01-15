import datetime
from django.conf import settings
from django.contrib.auth.models import AbstractUser, models
from django.db.models import CharField, IntegerField
from django.db.models.fields import FloatField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
import plaid


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


# class PlaidToken(models.Model):
#     access_token = models.CharField(max_length=64, default='')
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class BankAccount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.FloatField()


class BankTransaction(models.Model):
    amount = models.FloatField()
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
