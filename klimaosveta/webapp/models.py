from django.db import models

class BasicSite(models.Model):
    name = models.CharField()
    title = models.CharField()
    html = models.TextField()


class Messages(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField()
    email = models.EmailField()
    message = models.TextField()
    procesed = models.BooleanField(default=False)


