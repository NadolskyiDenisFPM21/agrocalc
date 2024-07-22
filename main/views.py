from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CropCalculation
from .forms import VariableCostsForm, ConstForm

import requests
from decimal import Decimal

@login_required
def index(request):
    
    rate_list = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json').json()
    
    
    crop = CropCalculation.objects.get(user=request.user)
    
    for rate in rate_list:
        if crop.rate.code == rate["cc"]:
            print(rate["cc"])
            crop.rate.rate = Decimal(rate["rate"]).quantize(Decimal('1.0000'))
            break
    if request.method == 'POST':
        var_form = VariableCostsForm(request.POST, instance=crop)
        if var_form.is_valid():
            var_form.save()
        const_form = ConstForm(request.POST, instance=crop)
        if const_form.is_valid():
            const_form.save()
        return redirect('index')
    else:
        var_form = VariableCostsForm(instance=crop)
        const_form = ConstForm(instance=crop)
    
    return render(request, 'index.html', {'var_form': var_form, 'const_form': const_form, 'crop': crop})


@login_required
def results(request):
    crop = CropCalculation.objects.get(user=request.user)
    
    return render(request, 'results.html', {'crop': crop})