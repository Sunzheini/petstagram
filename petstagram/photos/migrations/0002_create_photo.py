# Generated by Django 4.1.1 on 2022-10-11 09:09
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_alter_pet_slug'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True,
                                                 validators=[django.core.validators.MinLengthValidator(10)])),
                ('publication_date', models.DateField(auto_now=True)),
                ('tagged_pets', models.ManyToManyField(null=True, to='pets.pet')),
            ],
        ),
    ]
