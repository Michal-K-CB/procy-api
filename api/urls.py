from django.urls import include, path


from .views import AddressViewSet, TransactionViewSet, StakesInfoViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'wallets', AddressViewSet, basename='wallets')
router.register(r'transaction', TransactionViewSet, basename='transaction')
router.register(r'stakes_info', StakesInfoViewSet, basename='stakes_info')

urlpatterns = [
    path(r'', include(router.urls))
    ]
