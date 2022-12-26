from rest_framework import serializers
from .models import CountVehicles
from .main import detect

class CountVehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountVehicles
        fields = ('video', 'video_output', )

    def create(self, validated_data):
        video_vehicle = CountVehicles.objects.create(video=validated_data['video'])

        ## tinh toan tra lai ket qua

        vehicle = detect(video_vehicle)
        # vehicle.save()

        return video_vehicle
