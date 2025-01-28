from django import template

register = template.Library()

@register.filter
def to_range(value):
    """
    Convertit un entier en une plage (range) pour une boucle for dans les templates.
    """
    try:
        return range(int(value))
    except (TypeError, ValueError):
        return range(0)
