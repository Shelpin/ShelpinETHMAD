from django.urls import path
from .views import MerchantApiView, OngApiView

urlpatterns=[
    path("merchants/", MerchantApiView.as_view()),
    path("ongs/", OngApiView.as_view()),
]