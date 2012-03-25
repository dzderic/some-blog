from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.core.cache import cache

from . import utils

class Post(models.Model):
    title = models.CharField(max_length=255, default="")
    slug = models.SlugField()
    content = models.TextField(default="")
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    @property
    def html_content(self):
        cached = cache.get(self.html_cache_key)
        if cached:
            return cached
        else:
            html = utils.render_markdown(self.content)
            cache.set(self.html_cache_key, html, 3600)
            return html

    @property
    def html_cache_key(self):
        return 'blog:md-cache:%s' % self.slug

    def get_edit_url(self):
        return reverse('edit_post', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('delete_post', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        return reverse('view_post', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        else: # blow the cache
            cache.delete(self.html_cache_key)
        super(Post, self).save(*args, **kwargs)
