from django.contrib import admin
from api.models import Address, Transaction, Block, Stakes, StakingInfo, CoinBase, Inputs

admin.site.register(Address)
admin.site.register(Block)
admin.site.register(Transaction)
admin.site.register(Stakes)
admin.site.register(StakingInfo)
admin.site.register(CoinBase)
admin.site.register(Inputs)
