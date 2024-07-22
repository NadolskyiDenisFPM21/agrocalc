from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, CropCalculation, Currency

class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone_number', 'name', 'surname', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('name', 'surname', 'email', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, UserAdmin)


@admin.register(CropCalculation)
class CropCalculationAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Змінні', {'fields': ('seeds_price', 'rate', 'oil_price', 'oil_delivery', 'dealer', 'broker', 'oil_batch_weight', 'planned_profit')}),
        ('Константи тривалого періоду', {'fields': ('oil_content_base', 'oil_content_working', 'aditional_payment', 'oil_output',
                                                    'makukha_output', 'pellet_output', 'perfomance', 'price_makukha_without_bb',
                                                    'price_pellets_in_bb', 'vat_agro', 'vat_regular', 'tax_burden', 'vat_discount',
                                                    'electro_cost', 'electricity', 'oda', 'payroll',)}),
    )
    
    

@admin.register(Currency)    
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'text', 'rate')
