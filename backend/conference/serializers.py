from rest_framework import serializers
from . models import Conference


class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = ("name","theme","venue","shortdescription","resolution","presentation","images","abstract","cover","attendance","startdate","enddate","slug")
        read_only_fields = ["slug",]