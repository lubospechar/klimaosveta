from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CourseParticipant
from django.urls import reverse
from django.conf import settings
from django.utils.timezone import now
from datetime import timedelta
from django.core.mail import EmailMultiAlternatives

@receiver(post_save, sender=CourseParticipant)
def update_capacity_on_add(sender, instance, created, **kwargs):
    if created:
        course_detail = instance.course_detail
        course_detail.current_capacity += 1
        course_detail.save()

@receiver(post_delete, sender=CourseParticipant)
def update_capacity_on_delete(sender, instance, **kwargs):
    course_detail = instance.course_detail
    # Zde kontrolujeme, aby current_capacity neklesla pod 0
    if course_detail.current_capacity > 0:
        course_detail.current_capacity -= 1
        course_detail.save()


@receiver(post_save, sender=CourseParticipant)
def send_confirmation_email_and_set_expiration(sender, instance, created, **kwargs):
    pass
#     if created and not instance.confirm:
#         # Aktualizace instance s novým časem vypršení potvrzovacího kódu
#         instance.confirmation_code_expires = now() + timedelta(hours=24)
#         instance.save(update_fields=['confirmation_code_expires'])
#
#         # Vytvoření URL pro potvrzení
#         confirmation_url = reverse('confirm_email', args=[instance.confirmation_code])
#         full_url = f"{settings.SITE_URL}{confirmation_url}"
#
#         # Definování předmětu, těla zprávy a seznamu příjemců
#         subject = f'Přihlašení na kurz: {instance.course_detail.course.headline}'
#
#         months_cz = ["ledna", "února", "března", "dubna", "května", "června",
#                      "července", "srpna", "září", "října", "listopadu", "prosince"]
#
#         formatted_date = instance.course_detail.date.strftime(f"%-d. {months_cz[instance.course_detail.date.month - 1]} %Y")
#
#         # Vytvoření těla e-mailu
#         text_content = f'''Přihlašení na kurz: {instance.course_detail.course.headline}
# Pro {instance.course_detail.region}
# Dne: {formatted_date}
#
# Kliknutím na tento odkaz {full_url} potvrďte prosím svou účast. Dočasná rezervace je platná 24 hodin.'''
#
#         html_content = f'''<h1>Přihlašení na kurz: {instance.course_detail.course.headline}</h1>
# <h2>Pro: {instance.course_detail.region}</h2>
# <h2>Dne: {formatted_date}</h2>
# <p>Kliknutím na <a href="{full_url}">tento odkaz</a> potvrďte prosím svou účast. Dočasná rezervace je platná 24 hodin.</p>'''
#
#
#
#         recipient_list = [instance.email]
#
#         # Vytvoření e-mailu s alternativními reprezentacemi
#         email = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, recipient_list)
#         email.attach_alternative(html_content, "text/html")
#         email.send()
