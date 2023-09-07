from django.urls import path
from rest_framework import routers

from .views import (
    CategoryView,
    ) 

router=routers.DefaultRouter()
router.register("categories",CategoryView)

urlpatterns = [
    # path('register/', RegisterView.as_view()),

]+router.urls
