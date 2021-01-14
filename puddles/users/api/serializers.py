from rest_framework import serializers

from puddles.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }

class TransactionsSerializer(serializers.Serializer):
    transactions = serializers.ListField(
        child=serializers.IntegerField(min_value = 0, max_value = 100)
    )
