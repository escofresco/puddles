import json

from django.contrib.auth import get_user_model
from django.conf import settings
import plaid
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet

from users.api.serializers import TransactionsSerializer, UserSerializer

User = get_user_model()
class Transactions:
    def __init__(self, client):
        start_date = '{:%Y-%m-%d}'.format(datetime.datetime.now() +
                                          datetime.timedelta(-30))
        end_date = '{:%Y-%m-%d}'.format(datetime.datetime.now())
        try:
            pretty_print_response(transactions_response)
            self.transactions = client.Transactions.get(access_token,
                                                        start_date, end_date)
        except plaid.errors.PlaidError as e:
            self.transactions = self.format_error(e)

    def format_error(self, e):
        return {'error': {'display_message': e.display_message,
                          'error_code': e.code, 'error_type': e.type,
                          'error_message': e.message } }

    def pretty_print_response(response):
        print(json.dumps(response, indent=2, sort_keys=True))

class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class TransactionsViewSet(ViewSet):
    #serializer_class = TransactionsSerializer

    def list(self, request):
        client = plaid.Client(client_id=settings.PLAID_CLIENT_ID,
                      secret=settings.PLAID_SECRET,
                      environment=settings.PLAID_ENV,
                      api_version='2019-05-29')
        exchange_token_response = client.Item.public_token.exchange('[Plaid Link public_token]')
        access_token = exchange_token_response['access_token']

        stripe_response = client.Processor.stripeBankAccountTokenCreate(access_token, '[Account ID]')
        bank_account_token = stripe_response['stripe_bank_account_token']
        serializer = TransactionsSerializer(client)
        return Response(serializer.data)
