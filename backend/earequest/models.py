from django.db import models
from project.models import ProjectDonor
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.conf import settings


# Create your models here.

class ActivityRequest(models.Model):
    request = models.CharField(_("Request Name"), max_length=150)
    slug = models.SlugField(_("Slug"),editable=False,unique=True,blank=False)
    project = models.ForeignKey(ProjectDonor, verbose_name=_("Project Donor"), on_delete=models.CASCADE,related_name="donor")
    requestdate = models.DateField(_("Requesting Date"), auto_now=False, auto_now_add=False)
    description = models.TextField(_("Description"))
    requestedbby = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="requestedBy")
    approvedby = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="approvedBy")
    approveddate = models.DateField(_("End Date"), auto_now=False, auto_now_add=False)

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
    amount = models.DecimalField(_("Amount"), max_digits=10, decimal_places=2)
    frequency = models.IntegerField(_("Frequency"))