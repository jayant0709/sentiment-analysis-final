# Generated by Django 5.0.4 on 2024-07-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0008_auto_20240716_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatEmotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField()),
                ('response_text', models.CharField(blank=True, max_length=500, null=True)),
                ('emotion', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'chat_emotions',
            },
        ),
    ]
