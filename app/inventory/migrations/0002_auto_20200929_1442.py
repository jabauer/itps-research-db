# Generated by Django 3.1.1 on 2020-09-29 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='pub_places',
            field=models.ManyToManyField(blank=True, to='places.Location'),
        ),
    ]
