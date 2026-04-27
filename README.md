# Django Boilerplate Template

A production-ready Django project template with best practices, pre-configured apps, and a clean directory structure.

## Features

- **Django 6.0.4+**: Latest stable Django version
- **Pre-configured Apps**:
  - `django-environ` - Environment variable management
  - `django-health-check` - Application health checks
  - `django-mptt` - Hierarchical/tree data structure support
  - `django-tinymce` - Rich text editing
  - `django-view-breadcrumbs` - Breadcrumb navigation
  - `whitenoise` - Static file serving for production
- **Development Tools**:
  - Django Debug Toolbar
  - Django Extensions
  - IPython shell
- **Python 3.12+** - Modern Python with type hints support
- **Clean Project Structure** - Organized for scalability
- **Environment Configuration** - `.env` file support for sensitive data

## Project Structure

```
django-boilerplate/
├── manage.py              # Django management script
├── pyproject.toml         # Project configuration and dependencies
├── .env.example           # Example environment variables
├── db.sqlite3             # SQLite database
├── config/                # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # URL routing
│   ├── wsgi.py            # WSGI configuration
│   ├── asgi.py            # ASGI configuration
│   └── context_processors.py
├── apps/                  # Django applications
│   └── core/              # Core app (starting point)
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       ├── admin.py
│       ├── tests.py
│       └── templates/core/
│           └── index.html
├── templates/             # Project-wide templates
│   └── base.html          # Base template for inheritance
└── health_check_storage_test/  # Storage test configuration
```

## Getting Started

### Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) - Fast Python package installer and resolver

### Installation Steps

1. **Create a new Django project using this template**:
   ```bash
   django-admin startproject --template=https://github.com/kl4us/django-boilerplate/archive/refs/heads/main.zip myproject
   cd myproject
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and update the following:
   - `DEBUG=False` (for production)
   - `SECRET_KEY` - Generate a new secret key
   - `PROJECT_TITLE` - Your project name
   - `BRAND_NAME` - Your application brand name

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (admin account):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## Docker Deployment

This project includes a production-ready multistage Dockerfile and docker-compose configuration.

### Building and Running with Docker

1. **Build the Docker image**:
   ```bash
   docker build -t django-boilerplate .
   ```

2. **Run with Docker Compose** (recommended for development):
   ```bash
   docker-compose up
   ```
   The application will be available at `http://localhost:8000`

3. **Run the container directly**:
   ```bash
   docker run -p 8000:8000 django-boilerplate
   ```

### Docker Configuration

- **Multistage Build**: Optimizes final image size by separating build and runtime stages
- **Python 3.12-slim**: Minimal base image for reduced size and attack surface
- **Non-root User**: Runs as `appuser` (UID 1000) for enhanced security
- **Gunicorn + Uvicorn Workers**: Async-capable ASGI server for better performance
- **Health Checks**: Built-in health monitoring using Django's health check endpoint
- **Static Files**: Volume support for collected static files

### Environment Variables

Create a `.env` file or pass environment variables:
```bash
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com
DATABASE_URL=postgresql://user:password@db:5432/dbname
```

### Docker Compose Services

The `docker-compose.yml` includes:
- **web**: Django application running on port 8000
- **static_volume**: Shared volume for static files

To customize, edit `docker-compose.yml` to add database services (PostgreSQL, Redis, etc.).
   ```

   Access the application at `http://127.0.0.1:8000/`

## Usage

### Creating a New Django App

```bash
python manage.py startapp myapp
```

Add the app to `config/settings.py` in the `INSTALLED_APPS` list:
```python
INSTALLED_APPS = [
    # ...
    'apps.myapp',
]
```

### Database Migrations

Create migrations after model changes:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Admin Panel

Access the Django admin at `http://127.0.0.1:8000/admin/` with your superuser credentials.

### Static Files

Collect static files for production:
```bash
python manage.py collectstatic
```

### Shell Access

Use Django's enhanced shell with IPython:
```bash
python manage.py shell_plus
```

## Development

### Install Development Dependencies

```bash
pip install -e ".[dev]"
```

### Debug Toolbar

The Django Debug Toolbar is available in development mode at the bottom right of your browser.

### Running Tests

```bash
python manage.py test
```

### Code Organization

- Place models in `apps/*/models.py`
- Create views in `apps/*/views.py`
- Define URL patterns in `apps/*/urls.py`
- Create templates in `apps/*/templates/appname/`

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DEBUG` | `True` | Enable/disable debug mode |
| `SECRET_KEY` | `your-secret-key-here-change-in-production` | Django secret key |
| `PROJECT_TITLE` | `My Awesome Site` | Site title |
| `BRAND_NAME` | `SuperApp` | Application brand name |

Generate a secure secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Deployment

### Production Checklist

- [ ] Set `DEBUG=False` in `.env`
- [ ] Generate a new `SECRET_KEY` and keep it secure
- [ ] Configure a production database (PostgreSQL recommended)
- [ ] Set up proper logging
- [ ] Configure allowed hosts in `config/settings.py`
- [ ] Use a production WSGI server (Gunicorn, Uvicorn, etc.)
- [ ] Set up HTTPS/SSL
- [ ] Configure static and media file serving
- [ ] Set up database backups

### Running with Gunicorn

```bash
pip install gunicorn
gunicorn config.wsgi:application
```

## Build Template

This repository includes a template builder script. To create a clean template:

```bash
python build_template.py
```

This script:
- Copies the project to a clean template directory
- Removes development files and cache
- Preserves git history

## License

[Specify your license here]

## Support

For issues, questions, or contributions, please open an issue or contact the maintainers.

## References

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Best Practices](https://docs.djangoproject.com/en/stable/misc/design-philosophies/)
- [12 Factor App](https://12factor.net/)
