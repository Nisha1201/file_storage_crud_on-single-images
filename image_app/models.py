from django.db import models
from django.utils.safestring import mark_safe
# images = models.FileField()

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    def image_tag(self): # new
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.image))
    def __str__(self):
        return self.title