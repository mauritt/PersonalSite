from django.db import models


class Host(models.Model):
    name = models.CharField(max_length=20)
    base_site_URL = models.URLField()
    base_embed_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Project_type(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Project Type")


class Project(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    hidden = models.BooleanField(default = False)
    priority = models.IntegerField()
    url = models.URLField()
    host_code = models.CharField(max_length = 15, blank = True, null=True)
    host = models.ForeignKey('Host', blank=True, null=True)
    thumbnail_image = models.ImageField(upload_to='uploads/thumbnails')
    project_type = models.ForeignKey('Project_type')


    def __str__(self):
        return self.name
