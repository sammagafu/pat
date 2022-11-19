from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

# Create your models here.
class Conference(models.Model):
    name = models.CharField(_("Conference Name"), max_length=180)
    theme = models.CharField(_("Conference Theme"), max_length=180,default="conference theme")
    venue = models.CharField(_("Conference Venue and Location"), max_length=180,default="conference venue")
    slug = models.SlugField(_("Slug"),editable=False,unique=True,blank=False)
    shortdescription = models.TextField(_("Short Description"))
    resolution = models.FileField(_("Resolution"), upload_to="AGM/", max_length=100)
    presentation = models.URLField(_("Presentations"), max_length=200)
    images = models.URLField(_("Images"), max_length=200)
    abstract = models.FileField(_("Abstract Book"), upload_to=None, max_length=100)
    cover = models.ImageField(_("Project Cover Image"), upload_to="agm/cover/")
    attendance = models.IntegerField(_("Number of Attendance"))
    startdate = models.DateField(_("Start Date"), auto_now=False, auto_now_add=False)
    enddate = models.DateField(_("End Date"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = _("Conference")
        verbose_name_plural = _("Conferences")

    def __str__(self):
        return self.name

    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super().save()
