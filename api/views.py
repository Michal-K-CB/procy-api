from django_filters.rest_framework import DjangoFilterBackend

from api.models import Address, Transaction, Block, StakingInfo
from api.serializers import AddressSerializer, TransactionSerializer, BlockSerializer, StakesSerializer, \
    StakesInfoSerializer
from rest_framework import viewsets, mixins, filters
from rest_framework.pagination import LimitOffsetPagination


class SimpleViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    pass

class StandardResultsSetPagination(LimitOffsetPagination, ):
    default_limit = 20
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = None


class AddressViewSet(SimpleViewSet):
    serializer_class = AddressSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Address.objects.all()


class TransactionViewSet(SimpleViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ('created_at', )
    ordering = ('-created_at', )


class StakesInfoViewSet(SimpleViewSet):
    serializer_class = StakesInfoSerializer
    pagination_class = StandardResultsSetPagination
    queryset = StakingInfo.objects.all()
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ('created_at', )
    ordering = ('-created_at', )

