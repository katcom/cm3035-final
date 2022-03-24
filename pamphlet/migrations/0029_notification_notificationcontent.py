# Generated by Django 4.0.3 on 2022-03-23 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pamphlet', '0028_remove_notificationcontent_notification_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('FRI', 'Friend Request'), ('SYS', 'System Notification'), ('OTE', 'Friend Request')], default='OTE', max_length=3)),
                ('is_deleted', models.BooleanField(default=False)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NotificationContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_content', models.CharField(max_length=128, null=True)),
                ('notification', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='body', to='pamphlet.notification')),
            ],
        ),
    ]