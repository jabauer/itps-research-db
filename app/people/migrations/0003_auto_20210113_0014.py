# Generated by Django 3.1.1 on 2021-01-13 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20210113_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, choices=[('man', 'man'), ('woman', 'woman'), ('non-binary', 'non-binary'), ('other', 'other - describe in notes field'), ('unknown', 'unknown')], max_length=15, null=True),
        ),
    ]
