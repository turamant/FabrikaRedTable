# Generated by Django 3.2 on 2021-04-16 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='family',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='note',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]