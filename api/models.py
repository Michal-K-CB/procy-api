from django.db import models

# Create your models here.

class Address(models.Model):
    wallet_id = models.CharField(max_length=80)
    hash160 = models.CharField(max_length=80)
    version = models.CharField(max_length=80)
    balance = models.CharField(max_length=80)
    qrCode = models.CharField(max_length=80)
    scriptHash = models.CharField(max_length=80)
    isValid = models.BooleanField()
    isScript = models.BooleanField()
    isWitness = models.BooleanField()
    isMine = models.BooleanField()
    isWatchOnly = models.BooleanField()

    def __str__(self):
        return "%s the address" % self.wallet_id


class Block(models.Model):
    block_id = models.CharField(max_length=80)
    number = models.CharField(max_length=80)

class Inputs(models.Model):
    description = models.CharField(max_length=80)
    value = models.CharField(max_length=80)

class CoinBase(models.Model):
    hex = models.CharField(max_length=80)
    decoded = models.CharField(max_length=80)

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    address_from = models.ForeignKey(
        Address, related_name='address_from', on_delete=models.PROTECT, blank=True, null=True
    )
    address_to = models.ForeignKey(
        Address, related_name='address_to', on_delete=models.PROTECT
    )
    amount = models.CharField(max_length=80)
    type = models.CharField(max_length=80)
    block = models.ForeignKey(Block, on_delete=models.PROTECT)
    version = models.CharField(max_length=80)
    size = models.CharField(max_length=80)
    confirmation = models.CharField(max_length=80)
    fees_collected = models.CharField(max_length=80)
    inputs = models.ForeignKey(Inputs,  on_delete=models.PROTECT)
    coin_base = models.ForeignKey(CoinBase, on_delete=models.PROTECT)

    def __str__(self):
        return "%s the address" % self.transaction_id

class Stakes(models.Model):
    finished = models.IntegerField()
    ongoing = models.IntegerField()

class StakingInfo(models.Model):
    total_coins_staked = models.CharField(max_length=80)
    rewards_pool = models.CharField(max_length=80)
    staking_wallets = models.IntegerField()
    staking_contracts = models.IntegerField()
    stakes = models.ForeignKey(Stakes, on_delete=models.PROTECT)
    unstaked_ratio = models.IntegerField()
    total_predicted_rewards = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
