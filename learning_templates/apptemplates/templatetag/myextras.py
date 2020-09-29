from django import template
register=template.Library()
#@register.filter(name='cut')
def cut(value,arg):
    """
    THis cuts out allvalue "arg" from the string!
    :param value:
    :param arg:
    :return:
    """
    return value.replace(arg,'')
register.filter('cut',cut)


def sub(value,arg):
    return (value-arg)
register.filter('sub',sub)

