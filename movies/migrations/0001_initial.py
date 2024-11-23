# Generated by Django 5.1.3 on 2024-11-22 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('description', models.TimeField()),
                ('image', models.ImageField(upload_to='movie_images/')),
            ],
        ),
    ]
