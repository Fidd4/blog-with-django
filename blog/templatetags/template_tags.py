from django import template
from blog.models import Tag

register = template.Library()

@register.inclusion_tag('blog/templatetags/tags.html', takes_context=True)
def tag_list(context):
    return {'tags': Tag.objects.all()}
