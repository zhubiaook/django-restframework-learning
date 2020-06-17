from django.urls import path, include
from rest_framework import routers
from .views import SnippetViewSet, UserViewSet


route = routers.DefaultRouter()
route.register('snippets', SnippetViewSet)
route.register('users', UserViewSet)

urlpatterns = [
    path('', include(route.urls))
]

