from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CourseParticipant
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.utils.timezone import now
from datetime import timedelta

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
    if created and not instance.confirm:  # Kontrola pro novou neověřenou instanci
        # Nastavit confirmation_code_expires na 30 minut od aktuálního času
        instance.confirmation_code_expires = now() + timedelta(minutes=30)
        instance.save(update_fields=['confirmation_code_expires'])

        confirmation_url = reverse('confirm_email', args=[instance.confirmation_code])
        full_url = f"{settings.SITE_URL}{confirmation_url}"

        subject = 'Potvrďte svůj email'
        message = f'Prosím, potvrďte svůj email kliknutím na tento odkaz: {full_url}'
        recipient_list = [instance.email]

        send_mail(subject, message, 'enki@enki-projekty.cz', recipient_list)
