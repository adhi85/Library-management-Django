# Generated by Django 4.1.2 on 2022-10-13 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_user_book1_alter_user_book2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
