from rest_framework import serializers
from .models import ActivityRequestDetails,ActivityRequest

class ActivityRequestDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityRequestDetails
        fields = ['activity', 'service', 'amount','frequency']


class ActivityRequestSerializer(serializers.ModelSerializer):
    activity = ActivityRequestDetailsSerializer(many=True)

    class Meta:
        model = ActivityRequest
        fields = ['request','project','requestdate','description','requestedbby','approvedby','approveddate','activity']
    
    def create(self, validated_data):
        tracks_data = validated_data.pop('activity')

        arequest = ActivityRequest.objects.create(**validated_data)
        for track_data in tracks_data:
            ActivityRequestDetails.objects.create(activity=arequest, **track_data)
        return  arequest