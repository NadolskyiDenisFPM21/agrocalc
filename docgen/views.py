from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from django.conf import settings
from main.models import CropCalculation
from django.contrib.auth.decorators import login_required
import openpyxl


@login_required
def generate_pdf(request):
    # Создаем HttpResponse объект с типом содержимого PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="crop_calculation.pdf"'

    # Создаем PDF объект, используя HttpResponse в качестве "файла"
    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4
    y = height - 50
    # Путь к файлу шрифта
    font_path = settings.BASE_DIR / 'docgen/static/fonts/Roboto-Light.ttf'
    font_path2 = settings.BASE_DIR / 'docgen/static/fonts/Roboto-Bold.ttf'

    # Регистрация шрифта
    pdfmetrics.registerFont(TTFont('Roboto', font_path))
    pdfmetrics.registerFont(TTFont('RobotoBold', font_path2))

    # Получаем данные из модели
    calculation = CropCalculation.objects.get(user=request.user)

    p.setFont('RobotoBold', 10)
    p.drawString(50, y, "Змінні витрати")
    y -= 15
    
    
    fields = [
        ("Ціна насіння з ПДВ 14% грн/т", calculation.seeds_price),
        ("Курс валюти грн/валюта", calculation.rate),
        ("Ціна олії валюта/т", calculation.oil_price),
        ("Олія доставка, ПДВ 0% валюта/т", calculation.oil_delivery),
        ("Дилер, ПДВ 0% валюта/т", calculation.dealer),
        ("Брокер, ПДВ 0% грн/22 т", calculation.broker),
        ("Вага партії олії т", calculation.oil_batch_weight),
        ("Плановий прибуток на 1 тонні олії грн/т", calculation.planned_profit),
    ]
    

    
    p.setFont('Roboto', 10)
    for name, value in fields:
        p.drawString(50, y, name)
        p.drawString(470, y, str(value))
        y -= 15
    y -= 15
    
    
    p.setFont('RobotoBold', 10)
    p.drawString(50, y, "Константні показники")
    y -= 15
    
    fields2 = [
        ("Олійність базова %", calculation.oil_content_base),
        ("Олійність робоча %", calculation.oil_content_working),
        ("Доплата за 1% олійності грн/т%", calculation.aditional_payment),
        ("Вихід олії %", calculation.oil_output),
        ("Вихід макухи %", calculation.makukha_output),
        ("Вихід пелети %", calculation.pellet_output),
        ("Продуктивність т/сутки", calculation.perfomance),
        ("Ціна макухи без Біг Біга без ПДВ грн/т", calculation.price_makukha_without_bb),
        ("Ціна пелети в Біг Беге без ПДВ грн/т", calculation.price_pellets_in_bb),
        ("ПДВ агро %", calculation.vat_agro),
        ("ПДВ звичайний %", calculation.vat_regular),
        ("Податкове навантаження %", calculation.tax_burden),
        ("ПДВ дисконт %", calculation.vat_discount),
        ("Вартість електроенергії, з ПДВ 20% грн/кВт", calculation.electro_cost),
        ("Електроенергія кВт/сутки", calculation.electricity),
        ("ОПР грн/т", calculation.oda),
        ("ФОТ грн/сутки", calculation.payroll),
        ("Переробка грн/т", calculation.recycling),
    ]

    p.setFont('Roboto', 10)
    for name, value in fields2:
        p.drawString(50, y, name)
        p.drawString(470, y, str(value))
        y -= 15
    y -= 15


    p.setFont('RobotoBold', 10)
    # Выводим заголовки таблицы
    p.drawString(50, y, "Продукція")
    p.drawString(300, y, "Ціни без НДС")
    p.drawString(400, y, "Вага")
    p.drawString(470, y, "Всього без НДС")
    y -= 15

    # Выводим данные таблицы пользователя
    properties = [
        ("Насіння в переробку", calculation.price_seeds_in_processing, calculation.weight_seeds_in_processing, calculation.sum_seeds_in_processing),
        ("Переробка", calculation.price_recycling, calculation.weight_recycling, calculation.sum_recycling),

        ("Макуха", calculation.price_makuha, calculation.weight_makuha, calculation.sum_makuha),

        ("Пелета", calculation.price_pellete, calculation.weight_pellete, calculation.sum_pellete),

        ("Логістика по маслу", calculation.price_oil_logistics, calculation.weight_oil_logistics, calculation.sum_oil_logistics),

        ("Масло", calculation.price_oil, calculation.weight_oil, calculation.sum_oil),

        ("Налогове навантаження", "", "", calculation.sum_tax_burden),
        ("НДС втрати", "", "", calculation.sum_vat_losses),
        ("Ціна олії при плановому прибутку", "", "", calculation.oil_price_at_planned_profit),
        ("Фінансовий результат", calculation.price_financial_results, calculation.weight_financial_results, calculation.sum_financial_results),
    ]
    p.setFont('Roboto', 10)
    for prop_name, prop_value1, prop_value2, prop_value3 in properties:
        p.drawString(50, y, prop_name)
        p.drawString(300, y, str(prop_value1))
        p.drawString(400, y, str(prop_value2))
        p.drawString(470, y, str(prop_value3))
        y -= 15

    y -= 15
    p.setFont('RobotoBold', 10)
    p.drawString(250, y, "НДС")
    y -= 15

    properties2 = [
        ("Насіння в переробку", "", "", calculation.vat_seeds_in_processing),
        ("Переробка", "", "", calculation.vat_recycling),
        ("Насіння в переробку", "", "", calculation.sum_vat_credit),
    ]
    p.setFont('Roboto', 10)
    for prop_name, prop_value1, prop_value2, prop_value3 in properties2:
        p.drawString(50, y, prop_name)
        p.drawString(300, y, str(prop_value1))
        p.drawString(400, y, str(prop_value2))
        p.drawString(470, y, str(prop_value3))
        y -= 15
    
    # Заканчиваем PDF
    p.showPage()
    p.save()

    return response



def set_column_widths(sheet):
    for column_cells in sheet.columns:
        max_length = 0
        column = column_cells[0].column_letter  # Получаем букву столбца
        for cell in column_cells:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2)
        sheet.column_dimensions[column].width = adjusted_width




def generate_excel(request):
    # Получить пользователя из запроса (предполагая, что пользователь аутентифицирован)
    user = request.user

    # Получить данные модели, связанные с пользователем
    calculation = CropCalculation.objects.get(user=request.user)
    
    # Создать рабочую книгу и лист
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Crop Calculations"
    
    headers = [
        'Змінні витрати', 'Значення'
    ]
    
    fields = [
        ("Ціна насіння з ПДВ 14% грн/т", calculation.seeds_price),
        ("Курс валюти грн/валюта", calculation.rate),
        ("Ціна олії валюта/т", calculation.oil_price),
        ("Олія доставка, ПДВ 0% валюта/т", calculation.oil_delivery),
        ("Дилер, ПДВ 0% валюта/т", calculation.dealer),
        ("Брокер, ПДВ 0% грн/22 т", calculation.broker),
        ("Вага партії олії т", calculation.oil_batch_weight),
        ("Плановий прибуток на 1 тонні олії грн/т", calculation.planned_profit),
    ]
    
    ws.append(headers)
    
    for field in fields:
        ws.append(field)
        
    headers = [
        ('', ''),
        ('Константні значення', 'Значення')
    ]
    for header in headers:
        ws.append(header)
    
    fields2 = [
        ("Олійність базова %", calculation.oil_content_base),
        ("Олійність робоча %", calculation.oil_content_working),
        ("Доплата за 1% олійності грн/т%", calculation.aditional_payment),
        ("Вихід олії %", calculation.oil_output),
        ("Вихід макухи %", calculation.makukha_output),
        ("Вихід пелети %", calculation.pellet_output),
        ("Продуктивність т/сутки", calculation.perfomance),
        ("Ціна макухи без Біг Біга без ПДВ грн/т", calculation.price_makukha_without_bb),
        ("Ціна пелети в Біг Беге без ПДВ грн/т", calculation.price_pellets_in_bb),
        ("ПДВ агро %", calculation.vat_agro),
        ("ПДВ звичайний %", calculation.vat_regular),
        ("Податкове навантаження %", calculation.tax_burden),
        ("ПДВ дисконт %", calculation.vat_discount),
        ("Вартість електроенергії, з ПДВ 20% грн/кВт", calculation.electro_cost),
        ("Електроенергія кВт/сутки", calculation.electricity),
        ("ОПР грн/т", calculation.oda),
        ("ФОТ грн/сутки", calculation.payroll),
        ("Переробка грн/т", calculation.recycling),
    ]
    for field in fields:
        ws.append(field)
        
        
    headers = [
        ('', ''),
        ('Продукція', 'Ціни без НДС', 'Вага', 'Всього без НДС')
    ]
    for header in headers:
        ws.append(header)
        
    properties = [
        ("Насіння в переробку", calculation.price_seeds_in_processing, calculation.weight_seeds_in_processing, calculation.sum_seeds_in_processing),
        ("Переробка", calculation.price_recycling, calculation.weight_recycling, calculation.sum_recycling),

        ("Макуха", calculation.price_makuha, calculation.weight_makuha, calculation.sum_makuha),

        ("Пелета", calculation.price_pellete, calculation.weight_pellete, calculation.sum_pellete),

        ("Логістика по маслу", calculation.price_oil_logistics, calculation.weight_oil_logistics, calculation.sum_oil_logistics),

        ("Масло", calculation.price_oil, calculation.weight_oil, calculation.sum_oil),

        ("Налогове навантаження", "", "", calculation.sum_tax_burden),
        ("НДС втрати", "", "", calculation.sum_vat_losses),
        ("Ціна олії при плановому прибутку", "", "", calculation.oil_price_at_planned_profit),
        ("Фінансовий результат", calculation.price_financial_results, calculation.weight_financial_results, calculation.sum_financial_results),
    ]
    for property in properties:
        ws.append(property)
    
    set_column_widths(ws)
    
    # Создать HTTP ответ с Excel файлом
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=crop_calculations.xlsx'
    wb.save(response)

    return response