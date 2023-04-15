# Generated by Django 4.1.7 on 2023-04-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('obj_file', models.FileField(blank=True, null=True, upload_to='obj_files')),
                ('Flame_file', models.FileField(blank=True, null=True, upload_to='Flame_files')),
            ],
        ),
    ]
