# Generated by Django 5.0.6 on 2024-06-06 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_cash', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='BuyingSellingStocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=10)),
                ('amount', models.IntegerField()),
                ('stock_action', models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell')], max_length=5)),
                ('price', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='buying_stocks',
        ),
    ]
