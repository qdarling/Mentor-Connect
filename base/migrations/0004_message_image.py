# Generated by Django 4.2.4 on 2023-08-18 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_user_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="image",
            field=models.ImageField(null=True, upload_to="img/%y"),
        ),
    ]
