from django import template

register = template.Library()

@register.filter
def custom_intcomma(value):
    return f"{value:,}".replace(',', ' ')
