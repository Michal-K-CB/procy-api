# Generated by Django 3.1.4 on 2021-06-16 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_id', models.CharField(max_length=80)),
                ('hash160', models.CharField(max_length=80)),
                ('version', models.CharField(max_length=80)),
                ('balance', models.CharField(max_length=80)),
                ('qrCode', models.CharField(max_length=80)),
                ('scriptHash', models.CharField(max_length=80)),
                ('isValid', models.BooleanField()),
                ('isScript', models.BooleanField()),
                ('isWitness', models.BooleanField()),
                ('isMine', models.BooleanField()),
                ('isWatchOnly', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_id', models.CharField(max_length=80)),
                ('number', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='CoinBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hex', models.CharField(max_length=80)),
                ('decoded', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Inputs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=80)),
                ('value', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Stakes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finished', models.IntegerField()),
                ('ongoing', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.CharField(max_length=80)),
                ('type', models.CharField(max_length=80)),
                ('version', models.CharField(max_length=80)),
                ('size', models.CharField(max_length=80)),
                ('confirmation', models.CharField(max_length=80)),
                ('fees_collected', models.CharField(max_length=80)),
                ('address_from', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='address_from', to='api.address')),
                ('address_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='address_to', to='api.address')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.block')),
                ('coin_base', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.coinbase')),
                ('inputs', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.inputs')),
            ],
        ),
        migrations.CreateModel(
            name='StakingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_coins_staked', models.CharField(max_length=80)),
                ('rewards_pool', models.CharField(max_length=80)),
                ('staking_wallets', models.IntegerField()),
                ('staking_contracts', models.IntegerField()),
                ('unstaked_ratio', models.IntegerField()),
                ('total_predicted_rewards', models.CharField(max_length=80)),
                ('stakes', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.stakes')),
            ],
        ),
    ]
