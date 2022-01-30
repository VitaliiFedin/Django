from django.db import models


class Articles(models.Model):
    title = models.CharField("Title", max_length=50)
    announcment = models.CharField("Announcment",max_length=250)
    full_text = models.TextField("An acrticle")
    date = models.DateTimeField("Date of publication")

    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return f'/news/{self.id}'
# Create your models here.
