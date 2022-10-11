# Generated by Django 4.1.1 on 2022-10-11 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_alter_pet_slug'),
        ('photos', '0002_create_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='tagged_pets',
            field=models.ManyToManyField(blank=True, to='pets.pet'),
        ),
    ]