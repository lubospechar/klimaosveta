# Generated by Django 5.0.3 on 2024-03-17 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0012_region_coursedetail_courseparticipant"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="coursedetail",
            options={
                "verbose_name": "Jednotlivý kurz",
                "verbose_name_plural": "Jednotlivé kurzy",
            },
        ),
    ]
