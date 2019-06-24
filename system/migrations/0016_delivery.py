# Generated by Django 2.2.2 on 2019-06-24 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0015_auto_20190619_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=25)),
                ('customer', models.CharField(max_length=50)),
                ('customer_address', models.CharField(max_length=50)),
                ('user_name', models.CharField(default='Grasp Chemicals', max_length=25)),
                ('date_created', models.DateTimeField(verbose_name='date_published')),
            ],
        ),
    ]
