
# Generated by Django 3.2.13 on 2022-12-06 14:25


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_articles_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.CharField(choices=[('CS', 'CS'), ('알고리즘', '알고리즘'), ('진로', '진로'), ('오류', '오류'), ('기타', '기타')], max_length=50),
        ),
    ]
