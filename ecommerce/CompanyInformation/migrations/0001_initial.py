# Generated by Django 3.0 on 2020-10-11 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.BigIntegerField(unique=True)),
                ('of', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Contact Number',
                'verbose_name_plural': 'Contact Numbers',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('linkedIn_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('youtube_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Social Media',
                'verbose_name_plural': 'Social Medias',
            },
        ),
        migrations.CreateModel(
            name='CompanyInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('fax', models.CharField(blank=True, max_length=255, null=True)),
                ('post_box', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.ManyToManyField(blank=True, related_name='company_phone', to='CompanyInformation.ContactNumber')),
            ],
            options={
                'verbose_name': 'Company Information',
                'verbose_name_plural': 'Company Informations',
            },
        ),
    ]