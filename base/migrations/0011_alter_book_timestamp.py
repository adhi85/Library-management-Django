# Generated by Django 4.1.2 on 2022-10-14 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_book_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]