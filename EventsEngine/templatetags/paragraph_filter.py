from django import template
  
register = template.Library()
  
@register.filter()
def low(value):
    par = value.split("</p>")
    return par[0] + par[1]