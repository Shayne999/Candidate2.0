from django import template

register = template.Library()

@register.filter
def check_field(value):
    """Return the field value if it's not None or empty."""
    return value if value else ''
