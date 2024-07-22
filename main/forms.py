from django import forms
from .models import CropCalculation



class VariableCostsForm(forms.ModelForm):

    class Meta:
        model = CropCalculation
        fields = ['seeds_price', 'oil_price', 'oil_delivery', 'dealer', 'broker', 'oil_batch_weight', 'planned_profit', 'rate']




class ConstForm(forms.ModelForm):
    
    class Meta:
        model = CropCalculation
        fields = ('oil_content_base', 'oil_content_working', 'aditional_payment',
                  'oil_output', 'makukha_output', 'pellet_output', 'perfomance',
                  'price_makukha_without_bb', 'price_pellets_in_bb', 'vat_agro', 
                  'vat_regular', 'tax_burden', 'vat_discount', 'electro_cost', 
                  'electricity', 'oda', 'payroll',)
