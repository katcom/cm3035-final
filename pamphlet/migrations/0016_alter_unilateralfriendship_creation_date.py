# Generated by Django 4.0.3 on 2022-03-16 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pamphlet', '0015_remove_unilateralfriendshiprecord_is_deleted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unilateralfriendship',
            name='creation_date',
            field=models.DateTimeField(blank=True, editable=False),
        ),
    ]
