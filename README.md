# T2V Bot - Text to Video Generator

An experimental project for text-to-video generation using Django, Ollama LLM, HTML, and JavaScript.

## Features

- 🎬 Text-to-video generation interface
- 🤖 AI-powered prompt enhancement using Ollama
- 📊 Dashboard to track video generation requests
- 💻 Modern, responsive UI with HTML/CSS/JavaScript
- 🔄 Real-time status updates

## Technology Stack

- **Backend**: Django 4.2+
- **AI/LLM**: Ollama (for prompt enhancement)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Database**: SQLite (default, easily configurable)

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Ollama (optional, for prompt enhancement)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/govindvarmatn/t2v_bot.git
cd t2v_bot
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Run database migrations:
```bash
python manage.py migrate
```

4. Create a superuser (optional, for admin access):
```bash
python manage.py createsuperuser
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Open your browser and navigate to:
   - Main application: http://localhost:8000/
   - Admin panel: http://localhost:8000/admin/

## Setting up Ollama (Optional)

To enable prompt enhancement with Ollama:

1. Install Ollama from https://ollama.ai/
2. Pull the llama2 model:
```bash
ollama pull llama2
```
3. Start the Ollama service (it runs on http://localhost:11434 by default)

If Ollama is not available, the application will still work but without prompt enhancement.

## Usage

### Generate a Video

1. Navigate to the home page
2. Enter a descriptive text prompt (e.g., "A beautiful sunset over the ocean with waves crashing on the shore")
3. Click "Generate Video"
4. The system will:
   - Enhance your prompt using Ollama (if available)
   - Create a video generation request
   - Display the result with enhanced prompt and status

### View Dashboard

1. Click "Dashboard" in the navigation
2. View all your video generation requests
3. Click "View" on any request to see detailed information

### Admin Panel

Access the admin panel at `/admin/` to:
- Manage video requests
- View detailed statistics
- Update request statuses

## Project Structure

```
t2v_bot/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── .gitignore               # Git ignore rules
├── t2v_project/             # Django project settings
│   ├── settings.py          # Main settings
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI configuration
├── t2v_app/                 # Main application
│   ├── models.py            # Database models
│   ├── views.py             # Views and API endpoints
│   ├── urls.py              # App URL routing
│   ├── admin.py             # Admin configuration
│   └── templates/           # HTML templates
│       └── t2v_app/
│           ├── base.html    # Base template
│           ├── index.html   # Home page
│           └── dashboard.html # Dashboard page
└── static/                  # Static files
    ├── css/
    │   └── style.css        # Main stylesheet
    └── js/
        └── main.js          # JavaScript functionality
```

## API Endpoints

- `POST /api/generate/` - Generate a video from text prompt
  - Request body: `{"text_prompt": "your prompt here"}`
  - Response: `{"success": true, "request_id": 1, "status": "completed", ...}`

- `GET /api/status/<request_id>/` - Get status of a video request
  - Response: `{"id": 1, "status": "completed", "text_prompt": "...", ...}`

## Configuration

The main configuration options are in `t2v_project/settings.py`:

- `OLLAMA_API_URL`: URL for the Ollama API (default: `http://localhost:11434/api/generate`)
- `MEDIA_ROOT`: Directory for storing generated videos
- `STATIC_URL`: URL prefix for static files

## Development

To run the development server with auto-reload:
```bash
python manage.py runserver
```

To run tests (when available):
```bash
python manage.py test
```

## Contributing

This is an experimental project. Contributions, issues, and feature requests are welcome!

## License

This project is for experimental and educational purposes.

## Acknowledgments

- Built with Django
- Powered by Ollama for LLM capabilities
- Inspired by text-to-video generation research

## Notes

This is an experimental project demonstrating the integration of:
- Django web framework
- Ollama LLM for text processing
- HTML/CSS/JavaScript for frontend
- REST API design patterns

The actual video generation is currently a placeholder and would need integration with a real T2V model API for production use.
