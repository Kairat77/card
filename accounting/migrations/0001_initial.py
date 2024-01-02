# Generated by Django 4.2.6 on 2024-01-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Тема карточки обязательна.', max_length=200, verbose_name='Тема')),
                ('content_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на содержимое')),
                ('content_file', models.FileField(blank=True, null=True, upload_to='card_files/', verbose_name='Файл содержимого')),
            ],
        ),
    ]
