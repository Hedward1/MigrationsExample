# Generated by Django 3.2.14 on 2022-07-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=8)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('creation_date', models.DateField()),
                ('due_date', models.DateField()),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_address', models.CharField(max_length=50)),
                ('customer_city', models.CharField(max_length=50)),
                ('customer_zip_code', models.CharField(max_length=50)),
            ],
        ),
    ]
