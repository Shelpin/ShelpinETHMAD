from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile
import requests, json
from django.contrib.auth.models import User

#response = requests.post('https://api.blockcypher.com/v1/eth/main/adrs')


#response = requests.get('https://api.blockcypher.com/v1/eth/main/blocks/7').json()
response = requests.post('https://api.blockcypher.com/v1/eth/main/addrs?token=e864ae4d4cd54b1c9bc947989312b959').json()

url= "https://api.blockcypher.com/v1/eth/main/addrs?token=e864ae4d4cd54b1c9bc947989312b959"

#response = requests.get(url).json()
x= response["address"]
y = "0x"+x
print(f"**************************\nAddress: {y}\n*****************************************")

profiles = Profile.objects.all()

for profile in profiles:
    print(profile)
    if profile.address == None:
        print(profile.address)
        profile.address = y
        print(y)
        profile.save()






# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 6

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
