# Generated by Django 3.2.4 on 2021-06-26 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0002_evident_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='weakness',
            name='uuid',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
