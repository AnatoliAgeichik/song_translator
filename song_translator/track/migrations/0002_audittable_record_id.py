# Generated by Django 3.2 on 2021-06-22 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audittable',
            name='record_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]