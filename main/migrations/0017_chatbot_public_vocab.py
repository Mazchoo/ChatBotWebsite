# Generated by Django 3.1.4 on 2021-04-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_vocabalteration_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbot',
            name='public_vocab',
            field=models.JSONField(null=True),
        ),
    ]
