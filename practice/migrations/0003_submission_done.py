# Generated by Django 3.0.9 on 2020-08-05 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='done',
            field=models.CharField(max_length=4, null=True),
        ),
    ]