from rest_framework import serializers
from .models import ActivityRequestDetails,ActivityRequest

class ActivityRequestDetailsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = ActivityRequestDetails
        fields = ['id','activity', 'service', 'amount','frequency']
        read_only_fields = ("id",'activity')


class ActivityRequestSerializer(serializers.ModelSerializer):
    activities = ActivityRequestDetailsSerializer(many=True)

    class Meta:
        model = ActivityRequest
        fields = ['project','description','requestedbby','approvedby','approveddate', 'activities']
        read_only_fields = ("requestedby",)
    
    def create(self, validated_data):
        tracks_data = validated_data.pop('activities')

        arequest = ActivityRequest.objects.create(**validated_data)
        for track_data in tracks_data:
            ActivityRequestDetails.objects.create(activity=arequest, **track_data)
        return  arequest