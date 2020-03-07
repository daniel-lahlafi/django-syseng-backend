from django.db import models

class Toolkit(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(unique=True, max_length=512)
    url = models.URLField(max_length=256)
    content = models.TextField(blank=True)