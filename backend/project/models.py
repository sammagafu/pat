from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Project(models.Model):
    projectname = models.CharField(_("Project Name"), max_length=150)
    startdate = models.DateField(_("Starting Date"), auto_now=False, auto_now_add=False)
    shortdescription = models.TextField(_("Short Description"))
    specificObjective = models.TextField(_("Specific Objective"))
    enddate = models.DateField(_("End Date"), auto_now=False, auto_now_add=False)


    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.projectname

class ProjectGoal(models.Model):
    project = models.ForeignKey(Project, verbose_name=_(""), on_delete=models.CASCADE)
    goal = models.CharField(_("Project Goal"), max_length=150)
    results = models.CharField(_("Project Result"), max_length=180)

    class Meta:
        verbose_name = _("project goal")
        verbose_name_plural = _("project goals")

    def __str__(self):
        return self.goal
