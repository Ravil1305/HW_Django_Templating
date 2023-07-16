# Generated by Django 4.2.3 on 2023-07-15 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='catalog/', verbose_name='превью')),
                ('category', models.CharField(max_length=100, verbose_name='категория')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('date_of_creation', models.DateField(verbose_name='дата создания')),
                ('last_modified_date', models.DateField(verbose_name='дата последнего изменения')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]