from django import template
from django.contrib.admin.utils import get_object_display_name
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def to_repr(value):
    return get_object_display_name(value)
