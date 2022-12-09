from rest_framework import serializers
from .models import CountVehicles
from .core import count_vehicles

class CountVehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountVehicles
        fields = ('video', 'video_output', 'count', )
        extra_kwargs = {
            'count': {
                'required': False
            }
        }

    def create(self, validated_data):
        video_vehicle = CountVehicles.objects.create(video=validated_data['video'])

        ## tinh toan tra lai ket qua

        soluong = count_vehicles(video_vehicle.video, video_vehicle)
        video_vehicle.count = soluong
        video_vehicle.save()

        return video_vehicle
