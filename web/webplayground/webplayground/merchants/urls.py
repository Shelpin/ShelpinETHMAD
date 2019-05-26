from django.urls import path
from . import views
from django.conf.urls import url

from .views import MerchantListView


urlpatterns= [
    path("", MerchantListView.as_view(), name="list_merchants"),
    path("signupmerchant/", views.signupmerchantform, name = "signupmerchant")
]


