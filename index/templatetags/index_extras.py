from django import template

register = template.Library()

# @register.simple_tag
def integer_range(value):
    return range(1, value + 1)

register.filter('integer_range', integer_range)
