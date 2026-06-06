from django.contrib import admin
from .models import Category, Product, ProductScreenshot


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_en', 'slug', 'icon']
    prepopulated_fields = {'slug': ('name_en',)}
    search_fields = ['name', 'name_en']


class ProductScreenshotInline(admin.TabularInline):
    model = ProductScreenshot
    extra = 3
    fields = ['image', 'caption', 'order']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'product_type', 'price', 'is_featured', 'is_active', 'created_at']
    list_editable = ['is_featured', 'is_active']
    list_filter = ['is_active', 'is_featured', 'product_type', 'category']
    search_fields = ['name', 'short_description', 'full_description']
    prepopulated_fields = {'slug': ('name_en',)}
    ordering = ['-created_at']
    inlines = [ProductScreenshotInline]
    fieldsets = (
        ('معلومات أساسية', {
            'fields': ('name', 'name_en', 'slug', 'category', 'product_type', 'image')
        }),
        ('الوصف', {
            'fields': ('short_description', 'short_description_en', 'full_description', 'full_description_en')
        }),
        ('المميزات', {
            'fields': ('features', 'features_en')
        }),
        ('الروابط والسعر', {
            'fields': ('demo_url', 'download_url', 'price', 'price_label')
        }),
        ('الإعدادات', {
            'fields': ('is_featured', 'is_active')
        }),
    )


@admin.register(ProductScreenshot)
class ProductScreenshotAdmin(admin.ModelAdmin):
    list_display = ['product', 'caption', 'order']
    list_filter = ['product']
    ordering = ['product', 'order']
