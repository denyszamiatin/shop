from django.template import Library

register = Library()


@register.filter(name='dollar')
def convert_dollar(value):
    if value is None:
        return "Не определена"
    return str(value * 26.0)

@register.simple_tag
def hello():
    return "Hello"