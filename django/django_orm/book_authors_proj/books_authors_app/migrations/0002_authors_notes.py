# Generated by Django 2.2 on 2020-02-12 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notes',
            field=models.TextField(default='old authors'),
            preserve_default=False,
        ),
    ]
