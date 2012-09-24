from django.db import models
from django.template.defaultfilters import slugify


class NameSlugMixin(object):
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(NameSlugMixin, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Glossary(NameSlugMixin, models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'glossaries'


class Term(NameSlugMixin, models.Model):
    glossary = models.ForeignKey(Glossary, related_name='terms')
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    definition = models.TextField()

    class Meta:
        verbose_name_plural = 'glosses'
