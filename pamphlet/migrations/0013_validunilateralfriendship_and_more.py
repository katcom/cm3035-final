# Generated by Django 4.0.3 on 2022-03-16 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pamphlet', '0012_rename_friend_friendrequestentry_target'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValidUnilateralFriendship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendship', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='pamphlet.unilateralfriendship')),
            ],
        ),
        migrations.DeleteModel(
            name='UnilateralFriendshipRecord',
        ),
    ]
