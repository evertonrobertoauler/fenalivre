from django import template
register = template.Library()

@register.simple_tag
def target_link(page):
    if hasattr(page, 'novolink') and page.novolink.new_tab:
        return  'target="_blank"'
    else:
        return ""