# Generated by Django 4.1.3 on 2022-12-29 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0002_add_book_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='contactus',
        ),
    ]
