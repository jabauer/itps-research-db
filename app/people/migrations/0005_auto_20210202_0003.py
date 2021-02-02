# Generated by Django 3.1.1 on 2021-02-02 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_person_home_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='getty',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='viaf',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='wikipedia',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]