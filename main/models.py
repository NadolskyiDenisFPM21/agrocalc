from django.db import models
from users.models import User




class Currency(models.Model):
    code = models.CharField(max_length=3)
    text = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=10, decimal_places=4, verbose_name="Курс")
    
    def __str__(self):
        return str(self.text)
        



class CropCalculation(models.Model):

    user = models.ForeignKey("users.User", verbose_name="Користувач", on_delete=models.CASCADE)
    
    seeds_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна насіння з ПДВ 14% грн/т")
    rate = models.ForeignKey("main.Currency", verbose_name="Курс грн/валюта", on_delete=models.CASCADE)
    oil_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна олії валюта/т")
    oil_delivery = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Олія доставка, ПДВ 0% валюта/т")
    dealer = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Дилер, ПДВ 0% валюта/т")
    broker = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Брокер, ПДВ 0% грн/22 т")
    oil_batch_weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Вага партії олії т")
    planned_profit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Плановий прибуток на 1 тонні олії грн/т")
    
    oil_content_base = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Олійність базова %")
    oil_content_working = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Олійність робоча %")
    aditional_payment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Доплата за 1% олійності грн/т%")
    oil_output = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Вихід олії %")
    makukha_output = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Вихід макухи %")
    pellet_output = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Вихід пелети %")
    perfomance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Продуктивність т/сутки")
    price_makukha_without_bb = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна макухи без Біг Біга без ПДВ грн/т")
    price_pellets_in_bb = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна пелети в Біг Беге без ПДВ грн/т")
    vat_agro = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="ПДВ агро %")
    vat_regular = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="ПДВ звичайний %")
    tax_burden = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Податкове навантаження %")
    vat_discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="ПДВ дисконт %")
    electro_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Вартість електроенергії, з ПДВ 20% грн/кВт")
    electricity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Електроенергія кВТ/доба")
    oda = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ЗВВ  грн/т")
    payroll = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ФОТ грн/доба")
    
    
    
    @property
    def const_recycling(self):
        return round((self.payroll + self.electricity*self.electro_cost)/self.perfomance + self.oda, 2)
    
    # Семечка в переработку
    @property
    def price_seeds_in_processing(self):
        return round((self.seeds_price + (self.oil_content_working - self.oil_content_base)*self.aditional_payment)/(1 + self.vat_agro/100), 2)
    
    @property
    def weight_seeds_in_processing(self):
        return round(self.oil_batch_weight / self.oil_output * 100, 2)
    
    @property
    def sum_seeds_in_processing(self):
        return round(self.price_seeds_in_processing * self.weight_seeds_in_processing, 2)
    
    
    # Переработка
    @property
    def price_recycling(self):
        return round(self.sum_recycling / self.weight_recycling, 2)
    
    @property
    def weight_recycling(self):
        return self.weight_seeds_in_processing
    
    @property
    def sum_recycling(self):
        return round(self.const_recycling * self.weight_seeds_in_processing - self.vat_recycling, 2) 
    
    
    
    # Макуха
    @property
    def price_makuha(self):
        return self.price_makukha_without_bb
    
    @property
    def weight_makuha(self):
        return round(self.weight_seeds_in_processing * self.makukha_output / 100, 2)
    
    @property
    def sum_makuha(self):
        return round(self.price_makukha_without_bb * self.weight_makuha, 2)
    
    
    
    # Пелета
    @property
    def price_pellete(self):
        return self.price_pellets_in_bb
    
    @property
    def weight_pellete(self):
        return round(self.weight_seeds_in_processing * self.pellet_output / 100, 2)
    
    @property
    def sum_pellete(self):
        return round(self.price_pellete * self.weight_pellete, 2)
    
    
    # Логистика по маслу
    @property
    def price_oil_logistics(self):
        return round(self.sum_oil_logistics / self.weight_oil_logistics, 2)
    
    @property
    def weight_oil_logistics(self):
        return self.oil_batch_weight
    
    @property
    def sum_oil_logistics(self):
        return round(((self.oil_delivery + self.dealer) * self.rate.rate + self.broker / 22) * self.oil_batch_weight , 2)
    
    
    
    # Масло
    @property
    def price_oil(self):
        return self.oil_price
    
    @property
    def weight_oil(self):
        return self.oil_batch_weight
    
    @property
    def sum_oil(self):
        return round(self.price_oil * self.weight_oil * self.rate.rate, 2)
    
    
    
    # Налоговая нагрузка
    @property
    def sum_tax_burden(self):
        return round((self.sum_makuha + self.sum_oil + self.sum_pellete) * self.tax_burden / 100, 2)
    
    
    # Семечка в переработку vat
    @property
    def vat_seeds_in_processing(self):
        return round(self.sum_seeds_in_processing * self.vat_agro / 100, 2)
    
    # Переработка vat
    @property
    def vat_recycling(self):
        return round(self.electricity / self.perfomance * self.weight_seeds_in_processing * 
                     self.electro_cost / (1 + self.vat_regular / 100) * self.vat_regular / 100, 2)
    
    
    # ИТОГО налоговый кредит
    @property
    def sum_vat_credit(self):
        return round((self.vat_seeds_in_processing + self.vat_recycling) * (1 - self.vat_discount / 100), 2)
    
    
    # НДС потери
    @property
    def sum_vat_losses(self):
        return round((self.vat_seeds_in_processing + self.vat_recycling) * self.vat_discount / 100, 2)


    # Финансовый результат
    @property
    def price_financial_results(self):
        return round(self.sum_financial_results / self.weight_financial_results, 2)
    
    @property
    def weight_financial_results(self):
        return self.oil_batch_weight
    
    @property
    def sum_financial_results(self):
        return round(self.sum_oil - self.sum_oil_logistics + self.sum_makuha + self.sum_pellete - 
                     self.sum_recycling - self.sum_seeds_in_processing - self.sum_tax_burden - self.sum_vat_losses, 2)




    # Цена масла при плановой прибыли
    @property
    def oil_price_at_planned_profit(self):
        return round(((self.sum_oil - self.sum_financial_results) / self.oil_batch_weight + self.planned_profit) / self.rate.rate, 2)



    def __str__(self):
        return str(self.id)
    
    
    
