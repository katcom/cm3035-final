# Generated by Django 4.0.3 on 2022-03-15 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pamphlet', '0006_friendrequestentry_is_deleted'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CurrentFriendRequestEntry',
        ),
    ]
