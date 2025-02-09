from django import template
from django.contrib.admin.utils import display_for_value
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def to_object_display_value(value, avoid_quote=None):
    avoid_quote = avoid_quote == "avoid_quote"
    return display_for_value(str(value), "-", avoid_quote=avoid_quote)
