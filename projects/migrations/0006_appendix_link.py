# Generated by Django 4.2.1 on 2023-06-03 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_appendix'),
    ]

    operations = [
        migrations.AddField(
            model_name='appendix',
            name='link',
            field=models.CharField(default='default', max_length=400),
        ),
    ]
