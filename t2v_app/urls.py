from django.urls import path
from . import views

app_name = 't2v_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/generate/', views.generate_video, name='generate_video'),
    path('api/status/<int:request_id>/', views.get_video_status, name='get_video_status'),
]
