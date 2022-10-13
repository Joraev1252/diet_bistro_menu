from django.contrib import admin

from .models import MenuModel, CategoriesModel, PageView
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id')
    list_filter = ('id',)


admin.site.register(MenuModel, TodoAdmin)
admin.site.register(CategoriesModel)
admin.site.register(PageView)