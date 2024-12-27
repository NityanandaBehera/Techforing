# DRF Project Management API

A RESTful API for project management built with Django REST Framework.

## Prerequisites

- Python 3.8+
- pip
- Git

## Getting Started

1. Clone the repository:
```bash
https://github.com/NityanandaBehera/Techforing.git
cd project-management
```

2. Create and activate virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

5. Create superuser (optional):
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

## API Documentation

API documentation is available at:
- Swagger UI: `http://localhost:8000/api/swagger/`
- ReDoc: `http://localhost:8000/api/redoc/`

## Development

- Make sure to activate the virtual environment before running any commands
- Use `pip freeze > requirements.txt` to update dependencies
- Run tests with `python manage.py test`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details
