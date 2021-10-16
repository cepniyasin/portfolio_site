# Generated by Django 3.2.8 on 2021-10-15 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GisProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('Title', models.CharField(max_length=26)),
                ('Summary', models.TextField(blank=True, max_length=160, null=True)),
                ('URL', models.CharField(blank=True, max_length=1000, null=True)),
                ('Featured', models.BooleanField(default=False)),
                ('DetailViewImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('Description', models.TextField()),
                ('DetailViewImage_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('Title_2', models.CharField(blank=True, max_length=26, null=True)),
                ('Description_2', models.TextField(blank=True, null=True)),
                ('DetailViewImage_3', models.ImageField(blank=True, null=True, upload_to='')),
                ('Title_3', models.CharField(blank=True, max_length=26, null=True)),
                ('Description_3', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JSProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('Title', models.CharField(max_length=26)),
                ('Summary', models.TextField(blank=True, max_length=160, null=True)),
                ('URL', models.CharField(blank=True, max_length=1000, null=True)),
                ('Featured', models.BooleanField(default=False)),
                ('DetailViewImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('Description', models.TextField()),
                ('DetailViewImage_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('Title_2', models.CharField(blank=True, max_length=26, null=True)),
                ('Description_2', models.TextField(blank=True, null=True)),
                ('DetailViewImage_3', models.ImageField(blank=True, null=True, upload_to='')),
                ('Title_3', models.CharField(blank=True, max_length=26, null=True)),
                ('Description_3', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PythonProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('Title', models.CharField(max_length=26)),
                ('Summary', models.TextField(blank=True, max_length=160, null=True)),
                ('URL', models.CharField(blank=True, max_length=1000, null=True)),
                ('Featured', models.BooleanField(default=False)),
                ('DetailViewImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('Description', models.TextField()),
                ('DetailViewImage_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('Title_2', models.CharField(blank=True, max_length=26, null=True)),
                ('Description_2', models.TextField(blank=True, null=True)),
                ('DetailViewImage_3', models.ImageField(blank=True, null=True, upload_to='')),
                ('Title_3', models.CharField(blank=True, max_length=26, null=True)),
                ('Description_3', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
