from django.db import models
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

# Create your models here.
class GisProject(models.Model):
    Logo = models.ImageField(null=True, blank=True)
    Title       = models.CharField(blank=False, null=False, max_length=30)    # max_length = required
    Summary = models.TextField(blank=True, null=True, max_length=160)
    URL = models.CharField(blank=True, null=True, max_length=1000)
    Featured = models.BooleanField(default=False)  # null=True, default=True


    DetailViewImage = models.ImageField(null=True, blank=True)
    Section_Title_1 = models.CharField(blank=True, null=True, max_length=50)
    Description     = models.TextField(blank=False, null=False) #blank false means required?

    DetailViewImage_2 = models.ImageField(null=True, blank=True)
    Section_Title_2 = models.CharField(blank=True, null=True, max_length=50)
    Description_2 = models.TextField(blank=True, null=True)  # blank false means required?

    DetailViewImage_3 = models.ImageField(null=True, blank=True)
    Section_Title_3 = models.CharField(blank=True, null=True, max_length=50)
    Description_3 = models.TextField(blank=True, null=True)  # blank false means required?


    def get_absolute_urlHTML(self):
        return f"/GISprojects/{self.id}"

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={"id": self.id})   # f"/products{self.id}/"


class PythonProject(models.Model):
    Logo = models.ImageField(null=True, blank=True)
    Title       = models.CharField(blank=False, null=False, max_length=30)    # max_length = required
    Summary = models.TextField(blank=True, null=True, max_length=160)
    URL = models.CharField(blank=True, null=True, max_length=1000)
    Featured = models.BooleanField(default=False)  # null=True, default=True

    DetailViewImage = models.ImageField(null=True, blank=True)
    Section_Title_1 = models.CharField(blank=True, null=True, max_length=50)
    Description     = models.TextField(blank=False, null=False)

    DetailViewImage_2 = models.ImageField(null=True, blank=True)
    Section_Title_2 = models.CharField(blank=True, null=True, max_length=50)
    Description_2 = models.TextField(blank=True, null=True)

    DetailViewImage_3 = models.ImageField(null=True, blank=True)
    Section_Title_3 = models.CharField(blank=True, null=True, max_length=50)
    Description_3 = models.TextField(blank=True, null=True)


    def get_absolute_urlHTML(self):
        return f"/Python_projects/{self.id}"

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={"id": self.id})   # f"/products{self.id}/"


class JSProject(models.Model):
    Logo = models.ImageField(null=True, blank=True)
    Title       = models.CharField(blank=False, null=False, max_length=30)
    Summary = models.TextField(blank=True, null=True, max_length=160)
    URL = models.CharField(blank=True, null=True, max_length=1000)
    Featured = models.BooleanField(default=False)  # null=True, default=True

    DetailViewImage = models.ImageField(null=True, blank=True)
    Section_Title_1 = models.CharField(blank=True, null=True, max_length=50)
    Description     = models.TextField(blank=False, null=False)

    DetailViewImage_2 = models.ImageField(null=True, blank=True)
    Section_Title_2 = models.CharField(blank=True, null=True, max_length=50)
    Description_2 = models.TextField(blank=True, null=True)

    DetailViewImage_3 = models.ImageField(null=True, blank=True)
    Section_Title_3 = models.CharField(blank=True, null=True, max_length=50)
    Description_3 = models.TextField(blank=True, null=True)


    def get_absolute_urlHTML(self):
        return f"/JSprojects/{self.id}"

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={"id": self.id})   # f"/products{self.id}/"
from django.db import models