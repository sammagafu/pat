from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


# Create your models here.
class ProjectDonor(models.Model):
    donors = models.CharField(_("Donors Name"), max_length=150)
    website = models.URLField(_("Donors Website"))
    donorslogo = models.ImageField(_("Donors Logo"), upload_to="donors/logo/")

    class Meta:
        verbose_name = _("Project Donor")
        verbose_name_plural = _("Projects Donors")

    def __str__(self):
        return self.donors    

class Project(models.Model):
    cover = models.ImageField(_("Project Cover Image"), upload_to="project/cover/")
    projectname = models.CharField(_("Project Name"), max_length=150)
    slug = models.SlugField(_("Slug"),editable=False,unique=True,blank=False)
    donor = models.ForeignKey(ProjectDonor, verbose_name=_("Project Donor"), on_delete=models.CASCADE,related_name="projectdonor")
    startdate = models.DateField(_("Starting Date"), auto_now=False, auto_now_add=False)
    shortdescription = models.TextField(_("Short Description"))
    specificObjective = models.TextField(_("Specific Objective"))
    enddate = models.DateField(_("End Date"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.projectname

    def get_cover(self):
        if self.cover:
            return 'http://api.pediatrics.or.tz' + self.cover.url
        return ''

    def save(self):
        if not self.slug:
            self.slug = slugify(self.projectname)
        self.slug = slugify(self.projectname)
        super().save()

class ProjectGoal(models.Model):
    project = models.ForeignKey(Project, verbose_name=_("Project"), on_delete=models.CASCADE,related_name="goals")
    goal = models.CharField(_("Project Goal"), max_length=150)
    results = models.CharField(_("Project Result"), max_length=180)

    class Meta:
        verbose_name = _("project goal")
        verbose_name_plural = _("project goals")

    def __str__(self):
        return self.goal
