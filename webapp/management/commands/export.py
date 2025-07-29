import csv
from datetime import date
from django.core.management.base import BaseCommand
from webapp.models import CourseDetail, CourseParticipant


class Command(BaseCommand):
    help = "Exportuje proběhlé kurzy do stdout ve formátu CSV."

class Command(BaseCommand):
    help = 'Exportuje proběhlé kurzy do stdout ve formátu CSV.'

    def handle(self, *args, **kwargs):

        cp = CourseParticipant.objects.all()

        writer = csv.writer(self.stdout, quoting=csv.QUOTE_MINIMAL, delimiter=',')

        writer.writerow(['Jméno', 'Email', 'Telefon', 'Kurz', 'Kraj'])

        for p in cp:
            writer.writerow([
                f'{p.first_name} {p.last_name}',
                p.email,
                p.phone,
                p.course_detail.course.headline,
		p.course_detail.region.name
            ])
