# Generated by Django 4.1.3 on 2022-12-04 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0030_alter_category_options_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
