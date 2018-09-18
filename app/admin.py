from django.contrib import admin
from .models import TaskRequest,Profile
# Register your models here.

@admin.register(TaskRequest)
class TaskRequestAdmin(admin.ModelAdmin):
    '''Admin View for TaskRequest'''
    list_display = ('subject','created') 
    list_filter = ('subject','created')
    search_fields = ('subject','created','description')
    ordering = ('created','subject')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','image_tag','created')
    readonly_fields = ['image_tag']
    search_fields = ('user','profile_pic')
    ordering = ('created',)

