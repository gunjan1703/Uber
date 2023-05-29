from rest_framework import serializers
from users.models import (Student,)
class CreatedBySerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=('__all__')
class OrdersSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('__all__')

