from django import template

from Destinations_Catalogue.common.models import Like, Comment
from Destinations_Catalogue.profiles.models import CustomUser

register = template.Library()


@register.filter(name="filter_likes")
def filter_likes(value):
    return Like.objects.filter(destination_id=value.id).all().count() or 0


@register.filter(name="filter_comments")
def filter_comments(value):
    return Comment.objects.filter(destination_id=value.id).all()


@register.filter(name="filter_author_comment")
def filter_author_comment(value):
    return CustomUser.objects.filter(id=value.author_id).get()


@register.filter(name="filter_author")
def filter_author(value):
    return CustomUser.objects.get(id=value.creator_id).username
