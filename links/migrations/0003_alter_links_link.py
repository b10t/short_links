# Generated by Django 4.0.3 on 2022-03-04 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_remove_links_short_link_links_link_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='link',
            field=models.URLField(max_length=300, verbose_name='Ссылка'),
        ),
    ]