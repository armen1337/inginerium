# Generated by Django 3.1.7 on 2021-02-27 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210227_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='topheroimage',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='topheroimage',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок'),
        ),
    ]
