# Generated by Django 3.1.5 on 2021-03-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20210307_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colleagueimageconf',
            options={'verbose_name': 'Блок партнёра', 'verbose_name_plural': 'Блоки партнёров'},
        ),
        migrations.AlterField(
            model_name='heroimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='hero_images/', verbose_name='Картинка'),
        ),
    ]
