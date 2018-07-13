from django.urls import path
from catalog.views import (
    articles_list, articles_detail
)

# 2014/
urlpatterns = [
    path('', articles_list, name='articles_list'),
    path('<slug:id>/', articles_detail, name='articles_detail'),
]
