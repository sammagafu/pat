from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


# Create your models here.\
class Resource(models.Model):
    title = models.CharField(_("Document Name"), max_length=160)
    slug = models.SlugField(_("Slug"),editable=False,unique=True,blank=False)
    file = models.FileField(_("File Name"),upload_to="uploads/documents")
    published = models.BooleanField(_("Published"),default=False)
    created = models.DateTimeField(_("Created at"), auto_now=True,)
    description = models.TextField(_("Descriptions"))
    downloads = models.IntegerField(_("Number Downloads"),default=0)


    class Meta:
        verbose_name = _("Resource")
        verbose_name_plural = _("Resources")

    def __str__(self):
        return self.title

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        self.slug = slugify(self.title)
        super().save()
