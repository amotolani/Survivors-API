from rest_framework import serializers
from .models import Passenger


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ["uuid", "name", "passengerClass", "sex", "age", "siblingsOrSpousesAboard", "parentsOrChildrenAboard", "survived", "fare"]
