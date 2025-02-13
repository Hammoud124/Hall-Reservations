from django.urls import path
from rest_framework.routers import DefaultRouter

from main import views

router = DefaultRouter()
router.register('halls', views.HallModelViewSet)
router.register('clients', views.ClientModelViewSet)
urlpatterns = router.urls
