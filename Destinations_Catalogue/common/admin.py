from django.contrib import admin

from Destinations_Catalogue.common.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
