from django.views.generic import ListView
from .models import Merchant
from .forms import SignUpMerchantForm
from django.urls import reverse
from django.shortcuts import render, redirect


class MerchantListView(ListView):
    model = Merchant
    template_name = "merchant_list.html"




from django.shortcuts import render
from .forms import SignUpMerchantForm

def signupmerchantform(request):
    form= SignUpMerchantForm(request.POST or None)
    if form.is_valid():
        form.save()
  
        

        return redirect(reverse('signupmerchant')+'?ok')
    
    context= {'form': form }    

    return render(request, 'merchants/merchantsignupform.html', context)




"""
def signupmerchant(request):
    signup_form = SignUpMerchantForm()

    if request.method == "POST":
        signup_form = SignUpMerchantForm(data=request.POST)
        if signup_form.is_valid():
            signup_form.save()
            name = request.POST.get('name', '')
            description = request.POST.get('description', '')
            email = request.POST.get('email', '')
            donation = request.POST.get('donation', '')

            print(f"Name: {name} // Email: {email} ")
            


            return redirect(reverse('signupmerchant')+'?ok')


    return render(request, "merchants/merchantsignupform.html", {"form":signup_form})

    """