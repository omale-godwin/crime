# Generated by Django 3.2.4 on 2021-06-26 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evident',
            name='uuid',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]