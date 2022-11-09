from rest_framework import serializers
from .models import Project,ProjectDonor,ProjectGoal


class ProjectDonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDonor
        fields = ['donor','website','donorslogo']

class ProjectGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectGoal
        fields = ['pk','goal','results']


class ProjectSerializer(serializers.ModelSerializer):
    # projectdonor = ProjectDonorSerializer(many=True,read_only=True)
    goals = ProjectGoalSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        depth = 1
        fields = ['pk','slug','cover','projectname','shortdescription','specificObjective','startdate','enddate','donor','goals','get_cover']
