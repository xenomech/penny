# Generated by Django 4.2.17 on 2024-12-18 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="settings",
            name="theme",
            field=models.CharField(
                choices=[
                    ("light", "Light"),
                    ("dark", "Dark"),
                    ("cupcake", "Cupcake"),
                    ("emerald", "Emerald"),
                    ("autumn", "Autumn"),
                    ("forest", "Forest"),
                    ("retro", "Retro"),
                ],
                default="light",
                max_length=10,
            ),
        ),
    ]