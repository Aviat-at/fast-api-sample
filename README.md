# Django Project (myproject)

This repository contains a small Django project with a `books` app.

**Overview:**
- **Project root:** `myproject/`
- **Django app:** `books/` (models, serializers, views, urls)
- **Database:** SQLite (`myproject/db.sqlite3`) — pre-populated or local development DB

**Project structure (key files):**
- `myproject/manage.py` - Django management script
- `myproject/myproject/settings.py` - project settings
- `myproject/myproject/urls.py` - root URL configuration
- `myproject/books/` - app code (models, views, serializers, urls, tests)

Getting started
---------------

1. Create and activate a virtual environment (recommended):

```
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```
# If a requirements.txt exists, use it
pip install -r requirements.txt 2>/dev/null || pip install Django
```

3. Change into the Django project directory:

```
cd myproject
```

4. Apply migrations (creates or updates the local SQLite DB):

```
python manage.py migrate
```

5. (Optional) Create a superuser for the admin site:

```
python manage.py createsuperuser
```

Run the development server
--------------------------

From the `myproject/` directory run:

```
python manage.py runserver
```

By default the server runs at `http://127.0.0.1:8000/`.

Tests
-----

Run the Django test suite from `myproject/`:

```
python manage.py test
```

Notes
-----
- See `books/urls.py` for the app routes and available API endpoints.
- The repository includes a local SQLite database at `myproject/db.sqlite3` for convenience; remove or replace it for production use.
- Adjust the Python version in your environment as needed (project works with common Python 3.x versions).

If you want, I can also add a `requirements.txt` or expand the README with API examples.
