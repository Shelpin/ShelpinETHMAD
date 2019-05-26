from rest_framework import serializers

from merchants.models import Merchant
from ongs.models import Ong

class MerchantSerializer(serializers.ModelSerializer):

    class Meta:

        model = Merchant
        fields = ("name", "description", "email", "donation")

class OngSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Ong
        fields = ("name", "bank")