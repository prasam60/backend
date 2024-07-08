from rest_framework import routers
from .views import MembersViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'members', MembersViewSet)

urlpatterns = [
    path('', include(router.urls))
]