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
    shortcut = models.CharField(max_length=1, unique=True)
    image_on_left = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=1)
    image = models.ImageField(upload_to='courses_img')
    image_optimal = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1920, 100000)],
        format='JPEG',
        options={'quality': 80}
    )

    def __str__(self):
        return f'{self.shortcut} - {self.headline}'

    class Meta:
        verbose_name = "Typ kurzu"  # Lidsky čitelný název pro jednotný objekt
        verbose_name_plural = "Typy kurzů"  # Lidsky čitelný název pro množný počet objektů
        ordering = ['order']  # Objekty budou ve výchozím stavu řazeny podle 'order'



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


class Region(models.Model):
    name = models.CharField(max_length=255, verbose_name="Název kraje")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "kraj"
        verbose_name_plural = "kraje"

class CourseDetail(models.Model):
    region = models.ForeignKey('Region', on_delete=models.CASCADE, verbose_name="Kraj")
    date = models.DateField(verbose_name="Datum kurzu")
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name="Kurz")
    lector = models.ForeignKey('Lector', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Lektor")
    max_capacity = models.PositiveIntegerField(verbose_name="Maximální kapacita")
    current_capacity = models.PositiveIntegerField(verbose_name="Aktuální obsazenost")

    def __str__(self):
        return f"{self.region.name} - {self.date}"

    class Meta:
        verbose_name = "Jednotlivý kurz"
        verbose_name_plural = "Jednotlivé kurzy"

class CourseParticipant(models.Model):
    region = models.ForeignKey('CourseDetail', on_delete=models.CASCADE, verbose_name="Kraj")
    first_name = models.CharField(max_length=255, verbose_name="Jméno")
    last_name = models.CharField(max_length=255, verbose_name="Příjmení")
    email = models.EmailField(verbose_name="E-mail")
    phone = models.CharField(max_length=255, verbose_name="Telefon")
    confirm = models.BooleanField(default=False, verbose_name="Potvrzeno")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.region}"

    class Meta:
        verbose_name = "Účastník kurzu"
        verbose_name_plural = "Účastníci kurzu"

