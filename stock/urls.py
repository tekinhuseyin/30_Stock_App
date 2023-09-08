from django.urls import path
from rest_framework import routers

from .views import (
    CategoryView,
    BrandView,
    ProductView,
    FirmView,
    PurchasesView,
    ) 

router=routers.DefaultRouter()
router.register("categories",CategoryView)
router.register("brands",BrandView)
router.register("products",ProductView)
router.register("firms",FirmView)
router.register("purchases",PurchasesView)

urlpatterns = [
    # path('register/', RegisterView.as_view()),

]+router.urls
