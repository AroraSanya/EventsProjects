# Generated by Django 4.2 on 2023-04-17 05:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Events', '0007_alter_event_event_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join_events',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atendees', to='Events.event'),
        ),
        migrations.AlterField(
            model_name='join_events',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atendees', to=settings.AUTH_USER_MODEL),
        ),
    ]