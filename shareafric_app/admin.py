


from django.contrib import admin
from .models import (
    Feedback, Webdata, Client, Service, SkillRight, SkillLeft, 
    Summary, Education
)

# Feedback Admin
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')

# Webdata Admin
@admin.register(Webdata)
class WebdataAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'location', 'welcome_text')
    search_fields = ('phone', 'email', 'location')
    list_filter = ('location',)
    
# Client Admin
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'quote')
    search_fields = ('full_name',)

# Service Admin
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'icon', 'icon_color')
    search_fields = ('service_title',)
    list_filter = ('icon_color',)

# SkillRight Admin
@admin.register(SkillRight)
class SkillRightAdmin(admin.ModelAdmin):
    list_display = ('skill_title', 'skill_percent')
    search_fields = ('skill_title',)

# SkillLeft Admin
@admin.register(SkillLeft)
class SkillLeftAdmin(admin.ModelAdmin):
    list_display = ('skill_title', 'skill_percent')
    search_fields = ('skill_title',)

# Summary Admin
@admin.register(Summary)
class SummaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'about_me')
    search_fields = ('name', 'email')

# Education Admin
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('certificate', 'school', 'location', 'year_range')
    search_fields = ('certificate', 'school')
    list_filter = ('year_range',)


from django.contrib import admin
from .models import Category, Product, Review, ProductImage

# Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'icon', 'image')  # Removed 'created_at' field
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('icon',)
    ordering = ('name',)

# ProductImage Inline Admin
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Default number of empty forms to display
    fields = ('image', 'alt_text')
    max_num = 10  # Limit number of images a product can have

# Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'old_price', 'new_price', 'stock', 'created_at', 'updated_at')
    search_fields = ('name', 'slug', 'product_code')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category', 'stock', 'created_at')
    ordering = ('name',)
    
    # Add the product images inline
    inlines = [ProductImageInline]  # Use the correct inline model here
    
    def save_model(self, request, obj, form, change):
        if not obj.product_code:
            obj.product_code = obj.generate_product_code()  # Ensure the product code is set
        super().save_model(request, obj, form, change)

# Review Admin
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'rating', 'comment', 'created_at')
    search_fields = ('product__name', 'rating')
    list_filter = ('rating',)
    ordering = ('-created_at',)

# Registering ProductImage using decorator
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'alt_text')
    search_fields = ('product__name',)
    ordering = ('product',)
