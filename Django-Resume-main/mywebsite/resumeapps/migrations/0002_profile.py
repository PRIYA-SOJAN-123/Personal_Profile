# Generated by Django 4.2.2 on 2023-06-09 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('github', models.CharField(max_length=2550)),
            ],
        ),
    ]
