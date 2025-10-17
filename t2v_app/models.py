from django.db import models
from django.utils import timezone


class VideoRequest(models.Model):
    """Model to store text-to-video generation requests"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    text_prompt = models.TextField(help_text="Text prompt for video generation")
    enhanced_prompt = models.TextField(blank=True, null=True, help_text="Enhanced prompt from Ollama")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    video_url = models.CharField(max_length=500, blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Video Request {self.id} - {self.status}"
