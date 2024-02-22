from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
class BasicSite(models.Model):
    name = models.CharField()
    title = models.CharField()
    html = models.TextField()



class Message(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Jméno")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Zpráva")
    procesed = models.BooleanField(default=False)



class Course(models.Model):
    headline = models.CharField()
    html = models.TextField()
    image_on_left = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=1)
    image = models.ImageField(upload_to='courses_img')
    image_optimal = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1920, 100000)],
        format='JPEG',
        options={'quality': 80}
    )

class Lector(models.Model):
    name = models.CharField(max_length=255, verbose_name="Jméno")
    about = models.TextField(verbose_name="Text o sobě")
    image = models.ImageField(upload_to='lektori_obrazky/', verbose_name="Obrázek")
    image_optimal = ImageSpecField(source='image',
        processors=[ResizeToFit(800, 10000)],  # Použití ResizeToFit
        format='JPEG',
        options={'quality': 80}
    )

    image_admin = ImageSpecField(source='image',
        processors=[ResizeToFit(150, 10000)],  # Použití ResizeToFit
        format='JPEG',
        options={'quality': 50}
    )

    order = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Lektor"
        verbose_name_plural = "Lektoři"

