# Generated by Django 3.2.13 on 2022-12-10 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0002_alter_comment_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]