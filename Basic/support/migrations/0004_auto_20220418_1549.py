# Generated by Django 3.2.13 on 2022-04-18 15:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0003_alter_faq_updater'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='updater',
        ),
        migrations.AddField(
            model_name='faq',
            name='updater',
            field=models.ManyToManyField(blank=True, null=True, related_name='staff_user', to=settings.AUTH_USER_MODEL, verbose_name='최종 수정자'),
        ),
    ]
