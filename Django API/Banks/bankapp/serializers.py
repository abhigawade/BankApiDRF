from rest_framework import serializers
from .models import BankModel

class BankModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankModel
        fields = '__all__'  