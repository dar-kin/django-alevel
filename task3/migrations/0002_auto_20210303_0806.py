# Generated by Django 3.1 on 2021-03-03 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dislike',
            name='user',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]