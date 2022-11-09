from django.db import models
from project.models import ProjectDonor
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.conf import settings


# Create your models here.

class ActivityRequest(models.Model):
    project = models.ForeignKey(ProjectDonor, verbose_name=_("Project Donor"), on_delete=models.CASCADE,related_name="donor")
    requestdate = models.DateField(_("Requesting Date"), auto_now_add=True)
    description = models.TextField(_("Description"))
    approved = models.BooleanField(_("approved"),default=False)
    declined = models.BooleanField(_("declined"),default=False)
    requestedbby = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="requestedBy")
    approvedby = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="approvedBy",null=True,blank=True)
    approveddate = models.DateField(_("Approved Date"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = _("Activity Request")
        verbose_name_plural = _("Activity Requests")

    def __str__(self):
        return self.request

    def save(self):
        if not self.slug:
            self.slug = slugify(self.request)
        self.slug = slugify(self.request)
        super().save()

class ActivityRequestDetails(models.Model):
    activity = models.ForeignKey(ActivityRequest, verbose_name=_("Activity"), on_delete=models.CASCADE)
    service = models.CharField(_("Service or Product"), max_length=160)
    amount = models.DecimalField(_("Price Amount"), max_digits=10, decimal_places=2)
    frequency = models.IntegerField(_("Frequency"))