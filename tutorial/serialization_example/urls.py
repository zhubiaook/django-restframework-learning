from django.urls import path
from . import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    # path('snippets/<int:pk>/', views.snippet_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)