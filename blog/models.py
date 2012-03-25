from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

from . import utils

class Post(models.Model):
    title = models.CharField(max_length=255, default="")
    slug = models.SlugField()
    content = models.TextField(default="")
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    @property
    def html_content(self):
        return utils.render_markdown(self.content)

    def get_edit_url(self):
        return reverse('edit_post', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('delete_post', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        return reverse('view_post', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
