from django.shortcuts import render, redirect
from donations.forms import DonationForm
from .models import Donation

def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def donations(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = DonationForm()
    return render(request, 'donations.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')
