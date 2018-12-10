from rest_framework import serializers

from .models import CheckOut


class CheckOutSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckOut
        fields = ('id', 'total')