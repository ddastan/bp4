# Generated by Django 5.1.3 on 2024-11-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('pages', models.IntegerField()),
                ('cover', models.ImageField(upload_to='covers/')),
                ('language', models.CharField(max_length=50)),
            ],
        ),
    ]