from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings
import json
import requests
from .models import VideoRequest


from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def index(request):
    """Main page view"""
    return render(request, 't2v_app/index.html')


def dashboard(request):
    """Dashboard view showing all video requests"""
    # Limit to recent 100 requests for performance
    video_requests = VideoRequest.objects.all()[:100]
    return render(request, 't2v_app/dashboard.html', {'video_requests': video_requests})


@require_http_methods(["POST"])
def generate_video(request):
    """API endpoint to generate video from text"""
    try:
        data = json.loads(request.body)
        text_prompt = data.get('text_prompt', '')
        
        if not text_prompt:
            return JsonResponse({'error': 'Text prompt is required'}, status=400)
        
        # Create a new video request
        video_request = VideoRequest.objects.create(
            text_prompt=text_prompt,
            status='processing'
        )
        
        # Enhance the prompt using Ollama
        try:
            enhanced_prompt = enhance_prompt_with_ollama(text_prompt)
            video_request.enhanced_prompt = enhanced_prompt
            video_request.save()
        except Exception as e:
            video_request.enhanced_prompt = text_prompt
            video_request.save()
        
        # Simulate video generation (placeholder)
        # In a real implementation, this would call an actual T2V model
        video_request.status = 'completed'
        video_request.video_url = f'/media/videos/video_{video_request.id}.mp4'
        video_request.save()
        
        return JsonResponse({
            'success': True,
            'request_id': video_request.id,
            'status': video_request.status,
            'enhanced_prompt': video_request.enhanced_prompt,
            'video_url': video_request.video_url
        })
    
    except Exception as e:
        if 'video_request' in locals():
            video_request.status = 'failed'
            video_request.error_message = str(e)
            video_request.save()
        # Log the actual error for debugging but return generic message to user
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error generating video: {str(e)}", exc_info=True)
        return JsonResponse({'error': 'An error occurred while generating the video. Please try again.'}, status=500)


def enhance_prompt_with_ollama(text_prompt):
    """Enhance the text prompt using Ollama API"""
    try:
        payload = {
            "model": "llama2",
            "prompt": f"Enhance this text prompt for video generation, making it more descriptive and cinematic: {text_prompt}",
            "stream": False
        }
        
        response = requests.post(
            settings.OLLAMA_API_URL,
            json=payload,
            timeout=15
        )
        
        if response.status_code == 200:
            result = response.json()
            return result.get('response', text_prompt)
        else:
            return text_prompt
    except Exception:
        # If Ollama is not available, return the original prompt
        return text_prompt


@require_http_methods(["GET"])
def get_video_status(request, request_id):
    """Get the status of a video generation request"""
    video_request = get_object_or_404(VideoRequest, id=request_id)
    
    return JsonResponse({
        'id': video_request.id,
        'status': video_request.status,
        'text_prompt': video_request.text_prompt,
        'enhanced_prompt': video_request.enhanced_prompt,
        'video_url': video_request.video_url,
        'error_message': video_request.error_message,
        'created_at': video_request.created_at.isoformat(),
        'updated_at': video_request.updated_at.isoformat()
    })
