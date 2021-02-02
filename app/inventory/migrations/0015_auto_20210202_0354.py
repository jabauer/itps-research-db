# Generated by Django 3.1.1 on 2021-02-02 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_auto_20210202_0259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creator_role',
            options={'verbose_name': 'Creator Role'},
        ),
        migrations.AlterModelOptions(
            name='item_creator',
            options={'verbose_name': 'Creator'},
        ),
        migrations.AlterModelOptions(
            name='original_source',
            options={'verbose_name': 'Earlier Inventory', 'verbose_name_plural': 'Earlier Inventories'},
        ),
        migrations.AlterModelOptions(
            name='tgm_genre',
            options={'verbose_name': 'Genre (TGM)', 'verbose_name_plural': 'Genres (TGM)'},
        ),
        migrations.AlterField(
            model_name='item',
            name='short_title',
            field=models.CharField(max_length=50),
        ),
    ]
