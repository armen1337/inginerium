# Generated by Django 3.1.5 on 2021-03-07 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20210228_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColleagueImageConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Заголовок')),
                ('enabled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Блок коллег',
                'verbose_name_plural': 'Блоки коллег',
            },
        ),
        migrations.RemoveField(
            model_name='translate',
            name='director_am',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='director_en',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='director_name_am',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='director_name_en',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='director_name_ru',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='director_number',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='director_ru',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='external_am',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='external_en',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='external_name_am',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='external_name_en',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='external_name_ru',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='external_number',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='external_ru',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='finance_am',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='finance_en',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='finance_name_am',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='finance_name_en',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='finance_name_ru',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='finance_number',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='finance_ru',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='ingenier_am',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='ingenier_en',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='ingenier_name_am',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='ingenier_name_en',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='ingenier_name_ru',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='ingenier_number',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='ingenier_ru',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='sales_manager_am',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='sales_manager_en',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='sales_manager_name_am',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='sales_manager_name_en',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='sales_manager_name_ru',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='sales_manager_number',
        ),
        migrations.RemoveField(
            model_name='translate',
            name='sales_manager_ru',
        ),
        migrations.AlterField(
            model_name='topheroimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='top_hero_images/', verbose_name='Картинка'),
        ),
        migrations.CreateModel(
            name='ColleagueImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='colleague_images/', verbose_name='Картинка')),
                ('colleague_image_conf', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.colleagueimageconf')),
            ],
        ),
    ]