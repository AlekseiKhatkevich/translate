# Generated by Django 2.2.1 on 2019-06-03 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_to_text', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_file', models.FileField(upload_to='file_storage/', verbose_name='Audio files')),
                ('description', models.CharField(max_length=50, verbose_name='Audio File description')),
            ],
            options={
                'verbose_name': 'Audio File',
                'verbose_name_plural': 'Audio Files',
            },
        ),
    ]