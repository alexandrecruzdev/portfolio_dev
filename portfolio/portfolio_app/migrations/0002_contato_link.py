# Generated by Django 4.2.1 on 2023-06-09 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='link',
            field=models.CharField(default='', max_length=100),
        ),
    ]