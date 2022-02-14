# Generated by Django 3.2.12 on 2022-02-12 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
