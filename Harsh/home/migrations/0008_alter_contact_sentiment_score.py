# Generated by Django 4.2.1 on 2023-06-10 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_contact_recommend_remove_contact_skill_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='sentiment_score',
            field=models.FloatField(default=0.0),
        ),
    ]