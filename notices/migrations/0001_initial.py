

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', mdeditor.fields.MDTextField()),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notices_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
