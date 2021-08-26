# Generated by Django 3.2.5 on 2021-08-25 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0005_beerreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='average_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]