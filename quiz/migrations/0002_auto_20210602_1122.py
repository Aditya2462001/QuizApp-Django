# Generated by Django 3.2.2 on 2021-06-02 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(default='any of them', max_length=50),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
