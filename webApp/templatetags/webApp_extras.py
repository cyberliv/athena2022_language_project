from django import template

register = template.Library()

@register.filter
def first_letters(iterable):
    result = ""
    for item in iterable:
        result += item[0]

    return result