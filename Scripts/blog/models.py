from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    yazar = models.ForeignKey('auth.User')
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    yaratilis_tarihi = models.DateTimeField(default=timezone.now)
    yayinlanma_tarihi = models.DateTimeField(blank="true", null="true")

    def yayinla(self):
        self.yayinlanma_tarihi = timezone.now()
        self.save()

    @property
    def __str__(self):
        return self.baslik
