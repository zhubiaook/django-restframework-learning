"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework import routers
from quickstart import views as quickstart_views


route = routers.DefaultRouter()
route.register('user', quickstart_views.UserViewSets)
route.register('group', quickstart_views.GroupViewSets)


urlpatterns = [
    # path('', include(route.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('serialization_example.urls'))
]

