# Generated by Django 4.0.3 on 2022-03-04 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='links',
            name='short_link',
        ),
        migrations.AddField(
            model_name='links',
            name='link_id',
            field=models.CharField(blank=True, max_length=300, verbose_name='Идентификатор ссылки'),
        ),
    ]
