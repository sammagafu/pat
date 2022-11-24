from django.contrib import admin
from .models import ActivityRequest, ActivityRequestDetails
# Register your models here.
admin.site.register(ActivityRequest)
admin.site.register(ActivityRequestDetails)