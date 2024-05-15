

# rental serializers
from rest_framework import serializers

from .models import Rental


class RentalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rental
        fields = '__all__'
        read_only_fields = ['user']
        extra_kwargs = {
            'drone': {'required': True},
            'rental_date': {'required': True},
        }

    def create(self, validated_data):

        rental = Rental.objects.create(
            drone=validated_data['drone'],
            user=validated_data['user'],
            rental_date=validated_data['rental_date'],
        )

        return rental
