# Generated by Django 5.0.6 on 2024-07-22 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_cropcalculation_oil_batch_weight_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cropcalculation',
            name='recycling',
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='aditional_payment',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Доплата за 1% олійності грн/т%'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='broker',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Брокер, ПДВ 0% грн/22 т'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='dealer',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Дилер, ПДВ 0% валюта/т'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='electricity',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Електроенергія кВт/сутки'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='electro_cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Вартість електроенергії, з ПДВ 20% грн/кВт'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='makukha_output',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Вихід макухи %'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='oda',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ОПР грн/т'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='oil_batch_weight',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Вага партії олії т'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='oil_content_base',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Олійність базова %'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='oil_content_working',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Олійність робоча %'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='oil_delivery',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Олія доставка, ПДВ 0% валюта/т'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='oil_output',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Вихід олії %'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='oil_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна олії валюта/т'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='payroll',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ФОТ грн/сутки'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='pellet_output',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Вихід пелети %'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='perfomance',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Продуктивність т/сутки'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='planned_profit',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Плановий прибуток на 1 тонні олії грн/т'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='price_makukha_without_bb',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна макухи без Біг Біга без ПДВ грн/т'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='price_pellets_in_bb',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна пелети в Біг Беге без ПДВ грн/т'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='rate',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Курс валюти грн/валюта'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='seeds_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна насіння з ПДВ 14% грн/т'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='tax_burden',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Податкове навантаження %'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='vat_agro',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='ПДВ агро %'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='vat_discount',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='ПДВ дисконт %'),
        ),
        migrations.AlterField(
            model_name='cropcalculation',
            name='vat_regular',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='ПДВ звичайний %'),
        ),
    ]