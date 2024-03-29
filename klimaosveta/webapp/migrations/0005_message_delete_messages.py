# Generated by Django 5.0.2 on 2024-02-22 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0004_rename_mesages_messages"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(verbose_name="Jméno")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("message", models.TextField(verbose_name="Zpráva")),
                ("procesed", models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name="Messages",
        ),
    ]
