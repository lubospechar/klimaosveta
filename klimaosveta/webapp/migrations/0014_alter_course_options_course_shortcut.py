# Generated by Django 5.0.3 on 2024-03-17 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0013_alter_coursedetail_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="course",
            options={
                "ordering": ["order"],
                "verbose_name": "Typ kurzu",
                "verbose_name_plural": "Typy kurzů",
            },
        ),
        migrations.AddField(
            model_name="course",
            name="shortcut",
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
