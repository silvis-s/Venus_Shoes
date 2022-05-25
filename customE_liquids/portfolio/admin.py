from django.contrib import admin
from .models import Project, CategoryProd, Product

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'created')
    ordering = ('title',)
    search_fields = ('title',)
    date_hierarchy = 'created'

class CategoryProdAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmin)
admin.site.register(CategoryProd,CategoryProdAdmin)
admin.site.register(Product, ProductAdmin)
