from django import template

register = template.Library()

@register.simple_tag
def url_replace(request, filed, value):
    """
        replace Get parameter
    """
    url_dict = request.GET.copy()
    url_dict[filed] = value
    return url_dict.urlencode()