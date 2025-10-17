from django.contrib import admin
from .models import VideoRequest


@admin.register(VideoRequest)
class VideoRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'text_prompt', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'created_at']
    search_fields = ['text_prompt', 'enhanced_prompt']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Prompt Information', {
            'fields': ('text_prompt', 'enhanced_prompt')
        }),
        ('Status', {
            'fields': ('status', 'video_url', 'error_message')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
