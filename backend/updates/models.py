from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django_quill.fields import QuillField


# Create your models here.
class Updates(models.Model):
    title =  models.CharField(_("Title"), max_length=180)
    slug = models.SlugField(_("Slug"),unique=True,editable=False)
    cover = models.ImageField(_("Cover Image"), upload_to="blog/covers/")
    content = models.TextField()
    created = models.DateTimeField(_("Created at"), auto_now=True,)
    downloads = models.IntegerField(_("Number Of Views"),default=0,editable=False)
    membersonly = models.BooleanField(_("Members only"),default=False)

    class Meta:
        verbose_name = _("Updates")
        verbose_name_plural = _("Updatess")

    def __str__(self):
        return self.title
    
    def get_cover(self):
        if self.cover:
            return 'http://api.pediatrics.or.tz' + self.cover.url
        return ''

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        self.slug = slugify(self.title)
        super().save()
