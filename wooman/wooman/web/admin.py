from django.contrib import admin

from wooman.web.models import WomanModel


@admin.register(WomanModel)
class WomanAdmin(admin.ModelAdmin):
    pass
