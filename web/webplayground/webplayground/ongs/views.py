from django.views.generic import ListView
from .models import Ong

class OngListView(ListView):
    model = Ong
    template_name = "ong_list.html"
