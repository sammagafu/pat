from django.contrib import admin
from .models import Project,ProjectDonor,ProjectGoal
# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectDonor)
admin.site.register(ProjectGoal)