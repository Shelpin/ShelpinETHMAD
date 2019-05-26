from django.urls import path

from .views import OngListView

urlpatterns= [
    path("", OngListView.as_view(), name="list_ongs"),
]