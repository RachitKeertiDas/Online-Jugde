# Generated by Django 3.0.9 on 2020-08-05 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('statement', models.CharField(max_length=1000)),
                ('sample_testcase', models.CharField(max_length=1000)),
                ('sample_answer', models.CharField(max_length=1000)),
            ],
        ),
    ]
