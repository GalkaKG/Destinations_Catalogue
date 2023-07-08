from django import template

from Destinations_Catalogue.common.models import Like

register = template.Library()


@register.filter(name="filter_likes")
def filter_likes(value):
    return Like.objects.filter(destination_id=value.id).all().count() or 0
