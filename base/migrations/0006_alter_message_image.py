# Generated by Django 4.2.4 on 2023-08-18 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_alter_message_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="image",
            field=models.ImageField(
                default="default.jpeg", null=True, upload_to="img/%y"
            ),
        ),
    ]
