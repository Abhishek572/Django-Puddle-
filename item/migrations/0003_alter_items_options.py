# Generated by Django 5.1 on 2024-09-05 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_items'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='items',
            options={'ordering': ('name',), 'verbose_name_plural': 'Items'},
        ),
    ]
