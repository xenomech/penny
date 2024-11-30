# Generated by Django 5.1.3 on 2024-11-30 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_bankaccount_name_bankaccount_provider_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bankaccount",
            name="name",
            field=models.CharField(default="Untitled Bank Account", max_length=100),
        ),
        migrations.AlterField(
            model_name="bankaccount",
            name="provider",
            field=models.CharField(max_length=100),
        ),
    ]
