from django.contrib import admin

from Destinations_Catalogue.common.models import Comment, Like, Favorite


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main Information', {
            'fields': ('content',),
        }),
        ('Additional Information', {
            'fields': ('created_date',),
        }),
    )


@admin.register(Like)
class LikesAdmin(admin.ModelAdmin):
    search_fields = ['user', 'destination']


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass
