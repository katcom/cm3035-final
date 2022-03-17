# Generated by Django 4.0.3 on 2022-03-16 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pamphlet', '0013_validunilateralfriendship_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnilateralFriendshipRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('friendship', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pamphlet.unilateralfriendship')),
            ],
        ),
        migrations.DeleteModel(
            name='ValidUnilateralFriendship',
        ),
    ]
