


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


