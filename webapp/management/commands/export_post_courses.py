import csv
from datetime import date
from django.core.management.base import BaseCommand
from webapp.models import CourseDetail


class Command(BaseCommand):
    help = "Exportuje proběhlé kurzy do stdout ve formátu CSV."

class Command(BaseCommand):
    help = 'Exportuje proběhlé kurzy do stdout ve formátu CSV.'

    def handle(self, *args, **kwargs):
        # Filtruje proběhlé kurzy
        past_courses = CourseDetail.objects.filter(date__lt=date.today())

        # Vytváří CSV writer na stdout
        writer = csv.writer(self.stdout, quoting=csv.QUOTE_MINIMAL, delimiter=',')

        # Zapisuje hlavičku CSV
        writer.writerow(['Kraj', 'Datum', 'Kurz', 'Zkratka'])

        # Zapisuje data
        for course in past_courses:
            writer.writerow([
                course.region.name,
                course.date.strftime('%Y-%m-%d'),
                course.course.headline,
                course.course.shortcut
            ])
