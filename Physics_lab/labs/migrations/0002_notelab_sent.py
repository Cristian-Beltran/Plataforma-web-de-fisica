# Generated by Django 3.2.8 on 2021-10-29 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notelab',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]