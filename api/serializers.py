from rest_framework import serializers

from api.models import Address, Transaction, Block, Stakes, StakingInfo, Inputs, CoinBase


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ('id',)

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        exclude = ('id',)

class InputsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inputs
        exclude = ('id',)

class CoinBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinBase
        exclude = ('id',)


class TransactionSerializer(serializers.ModelSerializer):
    block = BlockSerializer(many=False, read_only=True)
    inputs = InputsSerializer(many=False, read_only=True)
    coin_base = CoinBaseSerializer(many=False, read_only=True)

    address_from = serializers.CharField(source='address_from.wallet_id', read_only=True)
    address_to = serializers.CharField(source='address_to.wallet_id', read_only=True)

    class Meta:
        model = Transaction
        exclude = ('id',)

class StakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stakes
        exclude = ('id',)


class StakesInfoSerializer(serializers.ModelSerializer):
    stakes = StakesSerializer(many=False, read_only=True)

    class Meta:
        model = StakingInfo
        exclude = ('id',)
